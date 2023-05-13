#!/bin/bash

cd /usr/src/ros2_ws
source "/opt/ros/dashing/local_setup.bash" -- && colcon build
source install/setup.bash
ros2 run fobo_yolo ros2_bridge.py &
pid1=$!
python3.8 /usr/src/ros2_ws/src/fobo_yolo/scripts/read_camera_yolo.py &
pid2=$!

# Wait for Ctrl+C
trap "kill $pid1 $pid2; exit" SIGINT

# Wait for processes to finish
wait $pid1
wait $pid2