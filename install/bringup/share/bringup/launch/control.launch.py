"""Launch file for lunabot control nodes."""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """Generate launch description for control nodes."""

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # x, y, z, qx, qy, qz, qw  (matches spawn in sim_lidar.launch.py)
    init_pose = LaunchConfiguration('init_pose')

    # Shared sensor mount parameters
    sensor_params = {
        'sensor_x': 0.15,
        'sensor_y': 0.0,
        'sensor_z': 0.6,
        'sensor_roll': 3.14159,
        'sensor_pitch': -0.785398,
        'sensor_yaw': 0.0,
    }

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation clock'
        ),
        DeclareLaunchArgument(
            'init_pose',
            default_value='[ 1.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]',
            description='Initial pose of the robot as [x, y, z, qx, qy, qz, qw]'
        ),

        # IMU node
        #Node(
        #    package='control',
        #    executable='imu_node',
        #    name='imu_node',
        #    parameters=[{'use_sim_time': False}],
        #    output='screen'
        #),

        # Static transform: world -> map (identity)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='world_to_map_tf',
            arguments=['0', '0', '0', '0', '0', '0', 'world', 'map'],
            parameters=[{'use_sim_time': use_sim_time}],
        ),

        Node(
            package='central_planner',
            executable='central_planner',
            name='central_planner',
            parameters=[{'use_sim_time': False}],
            output='screen'
        ),
        Node(
            package='pathing2',
            executable='pather_node',
            name='planner2',
            parameters=[{'use_sim_time': False}, {'init_pose': init_pose}],
            output='screen'
        ),
        Node(
            package='pathing',
            executable='map_gen',
            name='map_generator',
            parameters=[{'use_sim_time': False}],
            output='screen',
        ),
        Node(
            package='guidance',
            executable='guidance',
            name='guidance',
            parameters=[{'use_sim_time': use_sim_time}, {'init_pose': init_pose}],
            output='screen'
        ),
        #Node(
        #    package='control',
        #    executable='pose_integrator',
        #    name='pose_integrator',
        #    parameters=[{'use_sim_time': use_sim_time}, {'init_pose': init_pose}],
        #),
        Node(
            package='control',
            executable='robot_pose_publisher',
            name='robot_pose_publisher',
            parameters=[{'use_sim_time': use_sim_time}, {'init_pose': init_pose}],
        ),
        Node(
            package='auger',
            executable='control',
            name='auger_control',
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        Node(
            package='dump',
            executable='control',
            name='dump_control',
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        Node(
             package='control',
             executable='navigation_client',
             name='navigation_client',
             parameters=[{'use_sim_time': False}, {'init_pose': init_pose}],
         ),
        #Node(
        #    package='control',
        #    executable='gen_sensor_serv',
        #    name='sensor_node',
        #    parameters=[{'use_sim_time': use_sim_time}, {'init_pose': init_pose}],
        #),

        # KISS-ICP odometry (PRBonn) — scan-to-local-map LiDAR odometry.
        # Publishes /kiss/odometry. TF disabled to avoid clashing with the
        # static world->lidar frame in sim_lidar.launch.py.
        # Node(
        #     package='kiss_icp',
        #     executable='kiss_icp_node',
        #     name='kiss_icp_node',
        #     parameters=[{
        #         'use_sim_time': use_sim_time,
        #         'base_frame': '',          # use cloud frame_id as moving frame
        #         'lidar_odom_frame': 'odom_lidar',
        #         'publish_odom_tf': False,
        #         'publish_debug_clouds': False,
        #         'position_covariance': 0.1,
        #         'orientation_covariance': 0.1,
        #         'data.deskew': True,
        #         'data.max_range': 30.0,
        #         'data.min_range': 0.3,
        #         'mapping.max_points_per_voxel': 20,
        #         'adaptive_threshold.initial_threshold': 2.0,
        #         'adaptive_threshold.min_motion_th': 0.1,
        #         'registration.max_num_iterations': 500,
        #         'registration.convergence_criterion': 0.0001,
        #         'registration.max_num_threads': 0,
        #     }],
        #     remappings=[('pointcloud_topic', '/lidar/points/points')],
        #     output='screen'
        # ),

        # Wall localizer: wall-match drift correction on top of KISS-ICP.
        # Node(
        #     package='control',
        #     executable='wall_localizer',
        #     name='wall_localizer',
        #     parameters=[{
        #         'use_sim_time': use_sim_time,
        #         'voxel_leaf_size': 0.05,
        #         'transformation_epsilon': 1e-6,
        #         'pose_publish_rate': 30.0,
        #         'wall_match_rate': 1.0,
        #         'arena_width': 8.14,
        #         'arena_length': 9.14,
        #         'wall_height': 1.0,
        #         'wall_fitness_threshold': 0.3,
        #         'wall_max_correction_dist': 0.5,
        #         'wall_max_correction_yaw': 0.15,
        #         'wall_correction_weight': 0.05,
        #         'init_pose': init_pose,
        #         **sensor_params,
        #     }],
        #     output='screen'
        # ),

        # Obstacle Detector (RANSAC ground removal + clustering + crater detection)
        Node(
            package='control',
            executable='obstacle_detector',
            name='obstacle_detector',
            parameters=[{
                'use_sim_time': use_sim_time,
                'voxel_leaf_size': 0.05,
                'min_obstacle_z': 0.05,       # 5cm above ground = rock
                'max_obstacle_z': 0.5,
                'cluster_tolerance': 0.15,
                'min_cluster_size': 10,
                'max_cluster_size': 5000,
                'detect_rate': 5.0,
                'arena_width': 8.14,
                'arena_length': 9.14,
                'wall_margin': 0.3,
                'grid_resolution': 0.1,       # Match map_generator resolution
                'obstacle_inflation': 0.4,
                # Crater detection
                'crater_depth_threshold': 0.08,  # 8cm below ground = crater
                'ground_tolerance': 0.05,
                # Range limits
                'min_range': 0.3,
                'max_range': 12.0,
                # Robot self-filter box (in SENSOR frame)
                # Covers main robot body behind/below sensor
                'robot_box_min': [-0.5, -0.3, -0.8],
                'robot_box_max': [0.3, 0.3, 0.1],
                # Auger envelope (in SENSOR frame)
                # Conservative box covering all possible auger positions
                'auger_box_min': [0.0, -0.35, -1.0],
                'auger_box_max': [1.0, 0.35, 0.0],
                **sensor_params,
            }],
            output='screen'
        ),
    ])

