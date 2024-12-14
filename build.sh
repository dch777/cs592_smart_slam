#!/bin/bash

source /opt/ros/humble/setup.bash
rosdep install -y -i --from-paths ~/ros2_ws/src --skip-keys=stella_vslam
colcon build --symlink-install
