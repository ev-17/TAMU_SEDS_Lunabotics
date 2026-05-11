"""Launch file for simple_robot with e-CAM82 monocular camera in UCF arena."""

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
    pkg_lunabot_sim = get_package_share_directory('sim')
    pkg_lunabot_bringup = get_package_share_directory('bringup')

    # Paths - use UCF arena for visual environment
    world_file = os.path.join(pkg_lunabot_sim, 'worlds', 'ucf', 'ucf_arena.sdf')
    robot_model = os.path.join(pkg_lunabot_sim, 'models', 'simple_robot', 'model_camera.sdf')
    rviz_config = os.path.join(pkg_lunabot_bringup, 'rviz', 'camera_view.rviz')

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

    # Spawn robot with camera in Ignition
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
    # Camera image bridge - Ignition appends /image to the topic
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # Velocity commands
            '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
            # Odometry
            '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
            # Clock
            '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
            # Camera image - Ignition publishes to topic/image
            '/camera/image_raw@sensor_msgs/msg/Image[ignition.msgs.Image',
            # Camera info
            '/camera/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo',
        ],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # Static TF publisher for the camera frame
    # Frame ID from Ignition: spawned_model_name/link_name/sensor_name
    static_tf_camera = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_camera',
        arguments=[
            '--frame-id', 'world',
            '--child-frame-id', 'lunabot/camera_mount/front_camera',
            '--x', '1.45',  # Robot at x=1.0, camera at +0.45 from chassis center
            '--y', '-3.0',
            '--z', '0.15',  # Chassis at z=0.15, camera at z=0 relative to chassis
            '--roll', '0',
            '--pitch', '0',
            '--yaw', '0',
        ],
        parameters=[{'use_sim_time': use_sim_time}],
    )

    # RViz2 with camera visualization config
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    return LaunchDescription([
        declare_use_sim_time,
        gz_sim,
        spawn_robot,
        bridge,
        static_tf_camera,
        rviz,
    ])
