from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value='/home/surya/turtlebot3_ws/src/restaurant_world/maps/my_map.yaml',
            description='Full path to map file to load'
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        ),
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'map': LaunchConfiguration('map'),
            }],
            arguments=['--ros-args', '--params-file', LaunchConfiguration('map')]
        )
    ])

