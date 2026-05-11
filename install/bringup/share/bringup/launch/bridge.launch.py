"""Launch file for ROS-Ignition Gazebo bridge."""

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    """Generate launch description for Gazebo bridge."""

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    return LaunchDescription([

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation clock'
        ),

        # ROS-Ignition Bridge for cmd_vel (ROS -> Ignition)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='cmd_vel_bridge',
            arguments=[
                '/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist'
            ],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'
        ),

        # ROS-Ignition Bridge for odom (Ignition -> ROS)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='odom_bridge',
            arguments=[
                '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry'
            ],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'
        ),

        # Clock bridge (Ignition -> ROS)
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='clock_bridge',
            arguments=[
                '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock'
            ],
            output='screen'
        ),
    ])
