import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

# Motor 1
# PWM
GPIO.setup(33, GPIO.OUT)
pwm1 = GPIO.PWM(33, 490)
# Direction
dir1_pin = 31
GPIO.setup(dir1_pin, GPIO.OUT, initial=GPIO.HIGH)

# Motor 2
# PWM
GPIO.setup(32, GPIO.OUT)
pwm2 = GPIO.PWM(32, 490)
dir2_pin = 35
GPIO.setup(dir2_pin, GPIO.OUT, initial=GPIO.HIGH)


delta = 3
# Servo 1
incr_pin_1 = 11
dir_pin_1 = 12
GPIO.setup(incr_pin_1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(dir_pin_1, GPIO.OUT, initial=GPIO.HIGH)
angle_1 = 90

# Servo 2
incr_pin_2 = 15
dir_pin_2 = 16
GPIO.setup(incr_pin_2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(dir_pin_2, GPIO.OUT, initial=GPIO.HIGH)
angle_2 = 90


print("Interface to control 2 steppers and 2 servos")
print("Usage:\ncommand motor number")
print("Possible commands:\n")
print("Stepper control\n\ti: increase speed\n\tk: decrease speed\n\tf: go forward\n\tb: go backard")
print("Servo control\n\ts")
print("Example motor: i1 d2\nExaple servo s2")
print("\nPress Ctl C to quit \n")
dc1 = 0
dc2 = 0
    
pwm1.start(0)
pwm2.start(0)

def change_dc(dc, incr):
    dc = dc + incr
    if dc < 0:
        return (0)
    if dc > 100:
        return (100)
    return (dc)

try:
    while True:
        inpt = input()
        # Motor 1 logic
        if inpt == "i1":
            dc1 = change_dc(dc1, 10)
            print(dc1)
            pwm1.ChangeDutyCycle(dc1)
        if inpt == "k1":
            dc1 = change_dc(dc1, -10)
            print(dc1)
            pwm1.ChangeDutyCycle(dc1)
        if inpt == "b1":
            GPIO.output(dir1_pin, GPIO.LOW)
        if inpt == "f1":
            GPIO.output(dir1_pin, GPIO.HIGH)
        # Motor 2 logic
        if inpt == "i2":
            dc2 = change_dc(dc2, 10)
            print(dc2)
            pwm2.ChangeDutyCycle(dc2)
        if inpt == "k2":
            dc2 = change_dc(dc2, -10)
            print(dc2)
            pwm2.ChangeDutyCycle(dc2)
        if inpt == "b2":
            GPIO.output(dir2_pin, GPIO.LOW)
        if inpt == "f2":
            GPIO.output(dir2_pin, GPIO.HIGH)
        
        # Servo 1 logic
        if inpt == "s1":
            print("Type desrired angle (0-180), actual angle is: ", angle_1)
            angle = int(input())
            while(angle_1 != angle):
                if angle > angle_1:
                    GPIO.output(dir_pin_1, 1)
                    GPIO.output(incr_pin_1, 0)
                    time.sleep(10 / 1000)
                    GPIO.output(incr_pin_1, 1)
                    time.sleep(10 / 1000)
                    angle_1 += delta
                else:
                    GPIO.output(dir_pin_1, 0)
                    GPIO.output(incr_pin_1, 0)
                    time.sleep(10 / 1000)
                    GPIO.output(incr_pin_1, 1)
                    time.sleep(10 / 1000)
                    angle_1 -= delta
                print(angle_1)

        # Servo 2 logic
        if inpt == "s2":
            print("Type desrired angle (0-180), actual angle is: ", angle_2)
            angle = int(input())
            while(angle_2 != angle):
                if angle > angle_2:
                    GPIO.output(dir_pin_2, 2)
                    GPIO.output(incr_pin_2, 0)
                    time.sleep(10 / 1000)
                    GPIO.output(incr_pin_2, 1)
                    time.sleep(10 / 1000)
                    angle_2 += delta
                else:
                    GPIO.output(dir_pin_2, 0)
                    GPIO.output(incr_pin_2, 0)
                    time.sleep(10 / 1000)
                    GPIO.output(incr_pin_2, 1)
                    time.sleep(10 / 1000)
                    angle_2 -= delta
                print(angle_2)


except KeyboardInterrupt:
    print("Ctl C pressed - ending program")

pwm1.stop()                         # stop PWM
pwm2.stop()                         # stop PWM

GPIO.cleanup()                     # resets GPIO ports used back to 
