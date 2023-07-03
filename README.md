# FoBo
The idea of this project is to develop a robot capable to follow a human. It is formed by 2 wheels powered, a pi Camera and controlled by a Raspberry PI

# Desing
Model is created and it's stored en model folder. Where it is the 3D design of FoBo for a 3D printer

# Execute docker container in raspberry 
```bash
docker run -it --rm --privileged --device /dev/gpiomem -v /PATH/catkin_ws:/catkin_ws --name ros inigo183/rasp_ros_noetic /ros_entrypoint.sh /bin/bash
```
where PATH is the absolute path of folder (/home/user_name/fobo) if it is saved in root.

To acces same container in other terminal use
```bash
docker exec -it ros /ros_entrypoint.sh /bin/bash
```
