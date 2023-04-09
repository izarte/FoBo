FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3


ENV CUDA_HOME="/usr/local/cuda-10.2"
ENV CUDA_PATH="$CUDA_HOME"
ENV PATH="$CUDA_HOME/bin:$PATH"
ENV LD_LIBRARY_PATH="$CUDA_HOME/lib64:$CUDA_HOME/lib:$CUDA_HOME/extras/CUPTI/lib64:$CUDA_HOME/efa/lib:$LD_LIBRARY_PATH"
ENV LC_CTYPE=en_US.UTF-8

RUN apt-get update && apt-get install libxml2-dev libxslt-dev python3-dev cmake git -y
RUN git clone --recursive https://github.com/opencv/opencv-python.git
# ENV ENABLE_CONTRIB=1
# ENV ENABLE_HEADLESS=1

RUN pip3 install tqdm yacs amp timm scikit-build 
RUN pip3 install git+https://github.com/aleju/imgaug.git && pip3 install imgaug
RUN apt-get update && apt-get install ffmpeg -y
RUN pip3 install packaging typing_extensions pycocotools cityscapesscripts ffmpeg-python setuptools
RUN pip3 install ez_setup
RUN pip3 install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
WORKDIR opencv-python
RUN python3 setup.py bdist_wheel

# Install ros2
RUN apt-get update && apt-get install locales -y && apt-get install curl -y
RUN locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    export LANG=en_US.UTF-8
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu bionic main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN apt-get update && apt-get install ros-dashing-desktop -y

COPY siam-mot/apex /etc/apex
WORKDIR /etc/apex
RUN python3 setup.py install --cuda_ext --cpp_ext
COPY siam-mot/maskrcnn-benchmark /etc/maskrcnn-benchmark
WORKDIR /etc/maskrcnn-benchmark
RUN python3 setup.py build develop
COPY siam-mot /siam-mot
COPY v3_plugin_api.py /usr/local/lib/python3.6/dist-packages/imageio/core/v3_plugin_api.py
COPY dla34-ba72cf86.pth /root/.cache/torch/hub/checkpoints/dla34-ba72cf86.pth

WORKDIR /
COPY entrypoint.sh /entrypoint.sh
CMD ["./entrypoint.sh", "/bin/bash"]