FROM nvcr.io/nvidia/l4t-base:r32.7.1
# FROM nvcr.io/nvidia/l4t-tensorrt:r8.4.1.5-devel

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_CTYPE=en_US.UTF-8

RUN apt-get update && apt-get install -y \
      git \
      python3.8 python3.8-dev python3-pip \
      libopenmpi-dev libomp-dev libopenblas-dev libblas-dev libeigen3-dev

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install setuptools gdown

# pytorch 1.11.0
RUN gdown https://drive.google.com/uc?id=1hs9HM0XJ2LPFghcn7ZMOs5qu5HexPXwM
RUN python3.8 -m pip install torch-*.whl

# torchvision 0.12.0
RUN gdown https://drive.google.com/uc?id=1m0d8ruUY8RvCP9eVjZw4Nc8LAwM8yuGV
RUN python3.8 -m pip install torchvision-*.whl

RUN git clone https://github.com/ultralytics/ultralytics /usr/src/yolov8
WORKDIR /usr/src/yolov8
RUN python3.8 -m pip install -r requirements.txt
RUN python3.8 -m pip install ultralytics
RUN python3.8 -m pip install lap==0.4.0 websocket-client
RUN python3.6 -m pip install websockets

# Install onxxruntime_gpu adapted to this version
COPY onnxruntime_gpu-1.6.0-cp38-cp38-linux_aarch64.whl /tmp
RUN python3.8 -m pip install /tmp/onnxruntime_gpu-1.6.0-cp38-cp38-linux_aarch64.whl
# Upgrade to gcc-8/gcc+-8 and make to compile onnx and onnxsim
RUN   apt-get install gcc-8 g++-8 -y && \
      update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8 && \
      apt-get remove --purge --auto-remove cmake && \
      apt-get update && \
      apt-get install -y software-properties-common lsb-release libprotobuf-dev protobuf-compiler && \
      apt-get clean all && \
      wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null &&\
      apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" && \
      apt-get install kitware-archive-keyring -y && \
      rm /etc/apt/trusted.gpg.d/kitware.gpg && \
      apt-get install cmake -y && \
      python3.8 -m pip install onnx onnxsim

# Install ros2
RUN apt-get update && apt-get install locales -y && apt-get install curl -y
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu bionic main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN apt-get update && apt-get install ros-dashing-desktop -y
RUN apt update && apt install python3-colcon-common-extensions -y

ADD https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt /usr/src/ros2_ws/

WORKDIR /
COPY entrypoint.sh /entrypoint.sh
RUN /bin/bash -c "/entrypoint.sh"
COPY ros2_yolo8 /usr/src/ros2_ws
WORKDIR /usr/src/ros2_ws
RUN /bin/bash -c "/entrypoint.sh" "colcon build"

WORKDIR /
COPY start_yolo.sh /start_yolo.sh
CMD ["./start_yolo.sh"]