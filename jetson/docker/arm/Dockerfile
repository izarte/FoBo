FROM ubuntu:20.04

ENV LANG=en_US.UTF-8

RUN apt-get update && apt-get install locales -y && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common && \
    add-apt-repository universe

RUN apt-get update && apt-get install curl -y && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt-get update && apt-get upgrade -y &&\
     apt-get install ros-foxy-desktop python3-argcomplete -y &&\
     apt-get install ros-foxy-ros-base python3-argcomplete -y &&\
     apt-get install ros-dev-tools -y
RUN apt-get install python3-pip -y


COPY requierements.txt /tmp/requierements.txt
WORKDIR /tmp
RUN python3 -m pip install -r requierements.txt

WORKDIR /
COPY entrypoint.sh /entrypoint.sh
CMD ["./entrypoint.sh", "/bin/bash"]
