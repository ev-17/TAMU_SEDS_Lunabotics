"""Launch file for simple_robot with Unitree L1 LiDAR in UCF arena."""

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
    pkg_sim = get_package_share_directory('sim')
    pkg_bringup = get_package_share_directory('bringup')

    # Paths - use UCF arena for obstacles to see in point cloud
    world_file = os.path.join(pkg_sim, 'worlds', 'ucf', 'ucf_arena.sdf')
    robot_model = os.path.join(pkg_sim, 'models', 'simple_robot', 'model_lidar.sdf')
    rviz_config = os.path.join(pkg_bringup, 'rviz', 'lidar_view.rviz')

    # Launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation clock'
    )

    # Set Ignition resource path for models
    ign_resource_path = os.path.join(pkg_sim, 'models')
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

    # Spawn robot with LiDAR in Ignition (same position as UCF launch)
    # UCF arena ground is at z ≈ -0.25
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
    # Note: Ignition GPU LiDAR publishes to the topic specified in SDF <topic> tag
    # The sensor publishes PointCloudPacked messages
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # Velocity commands
            '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',
            # Odometry — NOT bridged; pose_integrator is sole /odom source
            # '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
            # Clock
            '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
            # LiDAR point cloud - Ignition appends /points to the topic name
            '/lidar/points/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked',
        ],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )

    # Static TF publisher for the lidar frame (matches point cloud frame_id)
    # The point cloud frame_id from Ignition is: spawned_model_name/link_name/sensor_name
    # We spawn with -name 'lunabot', so frame is: lunabot/lidar_sensor/lidar_l1
    # Sensor has: 180° roll (inverted) + 45° pitch (to shift -45/+45 to 0/90 hemisphere)
    static_tf_lidar = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_lidar',
        arguments=[
            '--frame-id', 'world',
            '--child-frame-id', 'lunabot/lidar_sensor/lidar_l1',
            '--x', '1.15',  # Approximate position in UCF arena
            '--y', '-3.0',
            '--z', '0.6',
            '--roll', '3.14159',   # Sensor is inverted (180°)
            '--pitch', '-0.785398', # Sensor pitched 45° to shift vertical range
            '--yaw', '0',
        ],
        parameters=[{'use_sim_time': use_sim_time}],
    )

    # RViz2 with LiDAR visualization config
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
        static_tf_lidar,
        rviz,
    ])