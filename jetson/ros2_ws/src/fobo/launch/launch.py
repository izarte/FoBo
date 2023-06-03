from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    nodes = []

    nodes.append(
        Node(
        package="fobo",
        executable="read_depth_camera.py",
        name="read_depth_camera",
        output="screen"
        )
    )
    
    nodes.append(
        Node(
        package="fobo",
        executable="camera_control.py",
        name="camera_control",
        output="screen"
        )
    )

    nodes.append(
        Node(
        package="fobo",
        executable="move_control.py",
        name="move_control",
        output="screen"
        )
    )

    nodes.append(
        Node(
        package="fobo",
        executable="move_motors_control.py",
        name="move_motors_control",
        output="screen"
        )
    )

    for node in nodes:
        ld.add_action(node)

    return ld