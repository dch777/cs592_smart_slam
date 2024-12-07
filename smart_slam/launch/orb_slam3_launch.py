from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="smart_slam",
            executable="camera",
        ),
        Node(
            package="ros2_orb_slam3",
            executable="mono_node_cpp",
            parameters=[
                {"node_name_arg": "mono_slam_cpp"},
                {"settings_file_path_arg": "/ros2_ws/src/smart_slam/config/"},
                {"voc_file_arg": "/ros2_ws/src/ros2_orb_slam3/orb_slam3/Vocabulary/ORBvoc.txt.bin"},
            ]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(
                    get_package_share_directory("turtlebot3_gazebo"),
                    "launch",
                    "turtlebot3_house.launch.py"
                )
            ])
        ),
    ])
