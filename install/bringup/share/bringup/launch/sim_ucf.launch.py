"""Launch file for simple_robot in UCF arena (competition environment)."""

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
    world_file = os.path.join(pkg_lunabot_sim, 'worlds', 'ucf', 'ucf_arena.sdf')
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

    # Launch Ignition Gazebo with UCF arena
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'--render-engine ogre -r {world_file}'}.items()
    )

    # Spawn robot in Ignition (positioned in starting area)
    # Note: UCF arena ground is at z ≈ -0.25 (collision box at z=-0.3 with height 0.1)
    # Robot tracks need ~0.15m clearance, so spawn at z=0.0 for gentle drop
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-file', robot_model,
            '-name', 'lunabot',
            '-x', '1.0',
            '-y', '-3.0',
            '-z', '0.0',
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

    # RViz2 (optional visualization)
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        declare_use_sim_time,
        gz_sim,
        spawn_robot,
        bridge,
        rviz,
    ])
