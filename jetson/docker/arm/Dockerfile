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

RUN apt-get update && apt-get install -y \
  libbullet-dev \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools

RUN python3 -m pip install -U \
  argcomplete \
  flake8-blind-except \
  flake8-builtins \
  flake8-class-newline \
  flake8-comprehensions \
  flake8-deprecated \
  flake8-docstrings \
  flake8-import-order \
  flake8-quotes \
  pytest-repeat \
  pytest-rerunfailures \
  pytest

RUN apt-get install --no-install-recommends -y \
  libasio-dev \
  libtinyxml2-dev

RUN apt-get install --no-install-recommends -y \
  libcunit1-dev

WORKDIR ros2_foxy
RUN mkdir src && vcs import --input https://raw.githubusercontent.com/ros2/ros2/foxy/ros2.repos src

ENV COLCON_PREFIX_PATH=/opt/ros
RUN apt-get upgrade -y && rosdep init && rosdep update && rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-5.3.1 urdfdom_headers"
RUN mkdir -p /opt/ros && colcon build --symlink-install

COPY requierements.txt /tmp/requierements.txt
WORKDIR /tmp
RUN python3 -m pip install -r requierements.txt

WORKDIR /opt/ros/foxy
# ENTRYPOINT [ ". ./setup.bash", "&&", "bash -c" ]

