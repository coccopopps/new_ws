import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    package_share_directory = get_package_share_directory('wheelchair_simv2')
    xacro_file = os.path.join(package_share_directory, 'urdf', 'wheelchair.xacro')

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_description',
            default_value=xacro_file,
            description='Path to robot description URDF or XACRO file'
        ),
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': xacro_file}],
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),
        
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link']
        ),
    ])
