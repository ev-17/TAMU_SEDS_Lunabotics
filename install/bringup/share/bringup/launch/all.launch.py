from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    launch_dir = PathJoinSubstitution([FindPackageShare('bringup'), 'launch'])

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    init_pose = LaunchConfiguration('init_pose', default='[ 1.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]')

    urdf_path = os.path.join(get_package_share_directory('sim'), 'models', 'simple_robot', 'model.urdf')

    with open(urdf_path) as file:
        robot_description = file.read()

    return LaunchDescription([
        DeclareLaunchArgument(
            'init_pose',
            default_value='[ 1.0, -3.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]',
            description='Initial pose of the robot as [x, y, z, qx, qy, qz, qw]'
    ),
    IncludeLaunchDescription(
        PathJoinSubstitution([launch_dir, "control.launch.py"]),
        launch_arguments={'init_pose': init_pose}.items()   
    ),
        IncludeLaunchDescription(
        PathJoinSubstitution([launch_dir, "static.launch.py"]),
    ),
    Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_description}]),
    ])
