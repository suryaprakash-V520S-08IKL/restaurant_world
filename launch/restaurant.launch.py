#!/usr/bin/env python3

import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Paths
    turtlebot3_desc_pkg = get_package_share_directory('turtlebot3_description')
    restaurant_world_pkg = get_package_share_directory('restaurant_world')

    world_file = os.path.join(restaurant_world_pkg, 'restaurant.world')
    urdf_file = os.path.join(turtlebot3_desc_pkg, 'urdf', 'turtlebot3_burger.urdf')

    # Read the URDF file directly
    with open(urdf_file, 'r') as infp:
        robot_description = {'robot_description': infp.read()}

    # Launch Gazebo with the world
    gazebo = ExecuteProcess(
        cmd=[
            'gazebo', '--verbose', world_file,
            '-s', 'libgazebo_ros_factory.so'
        ],
        output='screen',
        additional_env={
            'GAZEBO_MODEL_PATH': (
                '/usr/share/gazebo-11/models:' +
                '/opt/ros/humble/share/turtlebot3_gazebo/models:' +
                os.path.join(os.getenv('HOME'), 'turtlebot3_ws/src/restaurant_world/models')
            )
        }
    )

    # Robot state publisher node
    state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description],
        output='screen'
    )

    # Spawn the TurtleBot3 in Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'turtlebot3_burger',
            '-x', '0.0', '-y', '0.0', '-z', '0.1'
        ],
        output='screen'
    )

    # Delay spawning to let Gazebo load
    spawn_delay = TimerAction(
        period=5.0,
        actions=[spawn_entity]
    )

    # Return full launch description
    return LaunchDescription([
        gazebo,
        state_publisher,
        spawn_delay
    ])

