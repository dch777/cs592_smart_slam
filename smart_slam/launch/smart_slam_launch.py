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
            package="stella_vslam_ros",
            executable="run_slam",
            parameters=[
                {"publish_tf": False},
            ],
            arguments=[
                "-v", "/ros2_ws/src/smart_slam/config/orb_vocab.fbow",
                "-c", "/ros2_ws/src/smart_slam/config/pi_camera.yaml"
            ]
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(
                    get_package_share_directory(
                        "aws_robomaker_small_house_world"),
                    "launch",
                    "small_house.launch.py"
                )
            ]),
            launch_arguments={"gui": "True"}.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory(
                        "turtlebot3_gazebo"),
                    "launch",
                    "spawn_turtlebot3.launch.py"
                )
            ),
            launch_arguments={
                "x_pose": "0.0",
                "y_pose": "0.0"
            }.items()
        )
    ])
