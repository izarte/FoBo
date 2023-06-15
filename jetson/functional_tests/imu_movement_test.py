import Jetson.GPIO as GPIO
import time
import smbus
import simple_pid

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
# Truly is X axis in gyroscope
GYRO_ZOUT_H  = 0x43
# GYRO_ZOUT_H  = 0x47

 
def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
 
def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    
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

class Motor():
    def __init__(self, pin, direction, invert=False):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 490)
        self.dir = direction
        self.dc = 0
        self.i = invert
        GPIO.setup(self.dir, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.output(self.dir, GPIO.LOW)
        self.pwm.start(self.dc)

    def __del__(self):
        self.pwm.stop()

    def set_speed(self, dc):
        self.dc = dc
        if self.dc < 0:
            GPIO.output(self.dir, GPIO.HIGH)
            if self.i:
                GPIO.output(self.dir, GPIO.LOW)
            self.dc = -self.dc
        else:
            GPIO.output(self.dir, GPIO.LOW)
            if self.i:
                GPIO.output(self.dir, GPIO.HIGH)
        if self.dc > 100:
            self.dc = 100
        self.pwm.ChangeDutyCycle(self.dc)

def check_limits(value, minimum, maximum):
    if (value < minimum):
        return (minimum)
    if (value > maximum):
        return (maximum)
    return (value)

GPIO.setmode(GPIO.BOARD)
left_motor = Motor(33, 31, invert=True)
right_motor = Motor(32, 35)

Kp = 6
Ki = 2
Kd = 3

bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address
 
MPU_Init()
pid = simple_pid.PID(Kp, Ki, Kd)  # Initialize the PID controller with appropriate gains (Kp, Ki, Kd)

num_samples = 100
offset = 0
for _ in range(num_samples):
    offset += read_raw_data(GYRO_ZOUT_H)
    time.sleep(0.01)  # Delay between samples

prev_time = time.monotonic()
offset = offset / num_samples

yaw = 0

pid.output_limits = (-50, 50)  # Set the output limits of the PID controller
pid.setpoint = 0  # Set the desired setpoint for the PID controller (0 for forward movement)

speed = 20
try:
    while True:
        current_time = time.monotonic()

        gyro_z = read_raw_data(GYRO_ZOUT_H)
        
        Gz = (gyro_z - offset) / 131.0
        yaw = yaw + (Gz * (prev_time - current_time)) 

        control_signal = pid(yaw)

        left_speed = check_limits(speed + control_signal, 0, 100)
        right_speed = check_limits(speed - control_signal, 0, 100)
        print("left: ", left_speed, " right: ", right_speed)
        left_motor.set_speed(left_speed)
        right_motor.set_speed(right_speed)

        # print("Signal: {:.2f}".format(control_signal))

        prev_time = current_time
        time.sleep(0.01)  # Delay between readings
except KeyboardInterrupt:
    del(left_motor)
    del(right_motor)
    GPIO.cleanup()