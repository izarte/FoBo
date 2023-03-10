FROM osrf/ros:foxy-desktop
RUN sudo apt-get update && sudo apt-get upgrade -y && \
    sudo apt-get install ros-foxy-joint-state-publisher-gui -y && \
    sudo apt-get install ros-foxy-xacro -y && \
	sudo apt-get install ros-foxy-gazebo-ros-pkgs -y && \
	sudo apt install ros-foxy-turtlebot3* -y && \
	sudo apt-get install vim -y
CMD /ros_entrypoint.sh /bin/bash
