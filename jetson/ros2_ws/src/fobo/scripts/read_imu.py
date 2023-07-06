#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import time
import smbus
import simple_pid


from std_msgs.msg import Float32

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
# Truly is X axis in gyroscope
GYRO_ZOUT_H  = 0x43
# GYRO_ZOUT_H  = 0x47
Device_Address = 0x68 


class IMUReader(Node):
    def __init__(self):
        super().__init__('FoboMovement')
        self.offset = 0
        self.yaw = 0
        self.bus = smbus.SMBus(1)
        self.MPU_Init()
        self.calibrate()
        self.prev_time = time.monotonic()
        self.msg = Float32()
        self.pub = self.create_publisher(
            Float32,
            'yaw_orientation',
            10
        )
        timer_period = 0.01
        self.timer = self.create_timer(
            timer_period,
            self.timer_callback
        )

    def MPU_Init(self):
        #write to sample rate register
        self.bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        
        #Write to power management register
        self.bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        
        #Write to Configuration register
        self.bus.write_byte_data(Device_Address, CONFIG, 0)
        
        #Write to Gyro configuration register
        self.bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
        
        #Write to interrupt enable register
        self.bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, addr):
        #Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(Device_Address, addr)
        low = self.bus.read_byte_data(Device_Address, addr+1)
     
        #concatenate higher and lower value
        value = ((high << 8) | low)
         
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return -value

    def calibrate(self):
        num_samples = 100
        self.offset = 0
        for _ in range(num_samples):
            self.offset += self.read_raw_data(GYRO_ZOUT_H)
            time.sleep(0.01)  # Delay between samples

        prev_time = time.monotonic()
        self.offset = self.offset / num_samples

    def timer_callback(self):
        self.read_yaw()
        self.msg.data = self.yaw
        self.pub.publish(self.msg)

    def read_yaw(self):
        current_time = time.monotonic()

        gyro_z = self.read_raw_data(GYRO_ZOUT_H)
        Gz = (gyro_z - self.offset) / 131.0
        self.yaw = self.yaw + (Gz * (current_time - self.prev_time))
        self.prev_time = current_time

    
def main():
    rclpy.init()
    node = IMUReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()