import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():
    # Declare use_sim_time argument
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Get the path to the primary Xacro file
    pkg_path = os.path.join(get_package_share_directory('wheelchair_simv2'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'wheelchair.xacro')

    # Process the Xacro file
    robot_description_config = Command(['xacro ', xacro_file])

    # Node for robot_state_publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config,
                     'use_sim_time': use_sim_time}]
    )

    # Launch description
    return LaunchDescription([
        # Declare simulation time argument
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation time if true'),

        # Robot State Publisher Node
        node_robot_state_publisher
    ])
