from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'camera_link'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'camera_link', 'camera_color_frame'],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.51', '-0.2625', '0.36', '-3.1415', '0', '0', 'base_link', 'unilidar_imu_initial'],
        ),
         Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.0', '0.0', '0.0', '180.0', '0', '0', 'base_link', 'imu_link'],
        ),
        #Node(
         #   package='tf2_ros',
         #   excutable='static_transform_publisher',
          #  arugments=['51','-26.25','36.0','0','0','0', 'base_link', 'unitree_imu_initial'],
       # )
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=[
        #         '--x', '0.0',
        #         '--y', '0.0',
        #         '--z', '0.0',
        #         '--roll', '0.0',
        #         '--pitch', '0.0',
        #         '--yaw', '0.0',
        #         '--frame-id', 'camera_link',
        #         '--child-frame-id', 'camera_color_frame',
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=[
        #         '--x', '0.0',
        #         '--y', '0.0',
        #         '--z', '0.0',
        #         '--roll', '0.0',
        #         '--pitch', '0.0',
        #         '--yaw', '0.0',
        #         '--frame-id', 'camera_link',
        #         '--child-frame-id', 'camera_depth_frame',
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=[
        #         '--x', '0.0',
        #         '--y', '0.0',
        #         '--z', '0.0',
        #         '--roll', '0.0',
        #         '--pitch', '0.0',
        #         '--yaw', '0.0',
        #         '--frame-id', 'camera_link',
        #         '--child-frame-id', 'camera_color__optical_frame',
        #     ],
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=[
        #         '--x', '0.0',
        #         '--y', '0.0',
        #         '--z', '0.0',
        #         '--roll', '0.0',
        #         '--pitch', '0.0',
        #         '--yaw', '0.0',
        #         '--frame-id', 'camera_link',
        #         '--child-frame-id', 'camera_depth_optical_frame',
        #     ],
        # ),
    ])
