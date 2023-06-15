import smbus            #import SMBus module of I2C
import time
 
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
        return value
 
 
bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address
 
MPU_Init()
 
print (" Reading Data of Gyroscope and Accelerometer")

num_samples = 100
offset = 0
for _ in range(num_samples):
    offset += read_raw_data(GYRO_ZOUT_H)
    time.sleep(0.01)  # Delay between samples

offset = offset / num_samples
yaw = 0
prev_time = time.monotonic()
while True:
    current_time = time.monotonic()
    gyro_z = read_raw_data(GYRO_ZOUT_H)
     
    Gz = (gyro_z - offset) / 131.0
    if abs(Gz) > 0.02:
        yaw = yaw + (Gz * (current_time - prev_time))
    print ("Yaw=%.2f" %yaw)
    prev_time = current_time
    time.sleep(0.01)
# import time
# import board
# import adafruit_mpu6050
# import simple_pid

# Kp = 20
# Ki = 0
# Kd = 0

# i2c = board.I2C()  # Initialize the I2C bus
# mpu = adafruit_mpu6050.MPU6050(i2c)  # Initialize the MPU6050 sensor
# pid = simple_pid.PID(Kp, Ki, Kd)  # Initialize the PID controller with appropriate gains (Kp, Ki, Kd)

# num_samples = 100
# total_offset = [0.0, 0.0, 0.0]

# for _ in range(num_samples):
#     gyro_data = mpu.gyro
#     total_offset[0] += gyro_data[0]
#     total_offset[1] += gyro_data[1]
#     total_offset[2] += gyro_data[2]
#     time.sleep(0.01)  # Delay between samples

# avg_offset = [offset / num_samples for offset in total_offset]
# mpu.gyro_offset = avg_offset

# prev_time = time.monotonic()
# cumulative_yaw = 0.0

# pid.output_limits = (-50, 50)  # Set the output limits of the PID controller
# pid.setpoint = 0  # Set the desired setpoint for the PID controller (0 for forward movement)

# while True:
#     current_time = time.monotonic()
#     delta_time = current_time - prev_time

#     gyro_data = mpu.gyro
#     yaw = gyro_data[2] * delta_time  # Calculate yaw change by multiplying by time
#     cumulative_yaw += yaw

#     control_signal = pid(cumulative_yaw)

#     print("Signal: {:.2f}".format(control_signal))

#     prev_time = current_time
#     time.sleep(0.01)  # Delay between readings