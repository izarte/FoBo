# Fobo
This project is the final degree work in robotic engineering.
Fobo is a robot whose main task is to follow you to carry your heavy weights.

It is based on a webcam with 2 degrees of freedom thanks to 2 servomotors, which, using [YOLOv8] can detect and track people in its image. The camera will follow the objective person and the robot will move based on the servomotor's position. The robot also has a depth camera used to avoid obstacles.

![real]

# Model
All Fobo chassis have been modeled to be printed in a 3d printer. The total model can be found in [full-model]. To make the printing process easier divided model can be found in [divided-full-model].

Essential pieces to attach to a wooden board can be found in [final-real-pieces]

# Hardware
To create this robot it is necessary:
 1. NVIDIA Jetson Nano 2GB (5V 3A current)
 2. Arduino Uno
 3. Asus Xtion Pro Live
 4. Logitech C920 HD Pro Webcam
 5. 2x Stepper Motor NEMA17 (12V 2A current)
 6. 2x A4988 Stepper Driver
 7. 2x 1N4004 Diode
 8. 2x Servomotor mg945
 9. IMU MPU-6050

The following diagram shows how devices are connected

![circuit]

# Software
## Arduino

Arduino code can be found in [arduino]. This folder is a Platformio project. Code can be uploaded to Arduino via platformio.

## Jetson

### Prerequisites
1. Jetpack 4.6.2 (version L4T 32.7.1)
2. Docker (with docker-compose)

Go to [openni], a modified repository to execute in jetson nano based on [OpenNI2], and follow repository instructions.
Go to [ros2-ws] and execute the following commands to create a symbolic link to the dynamic library.
```
ln -s /usr/lib/OpenNI2
ln -s /usr/lib/libOpenNI2.so
```

After OpeNI installation, go to [jetson] folder and execute:
```
docker compose up
```

# Demo
Real demostration video:
<iframe width="560" height="315" src="https://www.youtube.com/embed/TPPlmqCqAJ4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>




[YOLOv8]: https://github.com/ultralytics/ultralytics
[real]: https://github.com/izarte/FoBo/blob/main/gallery/images/real_robot.jpeg
[full-model]: https://github.com/izarte/FoBo/tree/main/model/full_model
[divided-full-model]: https://github.com/izarte/FoBo/tree/main/model/divided_full_model
[final-real-pieces]: https://github.com/izarte/FoBo/tree/main/model/final_real_pieces
[circuit]: https://github.com/izarte/FoBo/blob/main/gallery/connections/circuit.jpg
[arduino]: https://github.com/izarte/FoBo/tree/main/arduino
[openni]: https://github.com/izarte/FoBo/tree/main/jetson/openni/OpenNI2-TX1/OpenNI2
[OpenNI2]: https://github.com/mikeh9/OpenNI2-TX1/tree/master/OpenNI2
[ros2-ws]: https://github.com/izarte/FoBo/tree/main/jetson/ros2_ws
[jetson]: https://github.com/izarte/FoBo/tree/main/jetson
