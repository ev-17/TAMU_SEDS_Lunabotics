"""Launch file for simple_robot in simple_world (testing environment)."""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    # Get package paths
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_lunabot_sim = get_package_share_directory('lunabot_sim')

    # Paths
    robot_model = os.path.join(pkg_lunabot_sim, 'models', 'simple_robot', 'model.sdf')

    # Launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation clock'
    )

    # Set Ignition resource path for models
    ign_resource_path = os.path.join(pkg_lunabot_sim, 'models')
    if 'IGN_GAZEBO_RESOURCE_PATH' in os.environ:
        os.environ['IGN_GAZEBO_RESOURCE_PATH'] += ':' + ign_resource_path
    else:
        os.environ['IGN_GAZEBO_RESOURCE_PATH'] = ign_resource_path

    #Launch Ignition Gazebo with simple world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'--render-engine ogre -r {world_file}'}.items()
    )

    # Spawn robot in Ignition
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-file', robot_model,
            '-name', 'lunabot',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.5',
        ],
        output='screen'
    )

    # ROS-Ignition Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
            '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
        ],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # Control nodes
    drive_controller = Node(
        package='lunabot_control',
        executable='drive_controller',
        name='drive_controller',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    pose_integrator = Node(
        package='lunabot_control',
        executable='pose_integrator',
        name='pose_integrator',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # Note: imu_node requires world->base_link TF which needs proper odometry->TF conversion
    # For now, we run without it. To enable: add odom->TF node or robot_state_publisher

    return LaunchDescription([
        declare_use_sim_time,
        # gz_sim,
        spawn_robot,
        bridge,
        drive_controller,
        pose_integrator,
    ])
