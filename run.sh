#!/bin/bash

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py & >/dev/null
# ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True & >/dev/null
# ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True & >/dev/null
# ros2 run rviz2 rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz & >/dev/null

bash
