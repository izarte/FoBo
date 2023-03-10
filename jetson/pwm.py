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

# Servo 1
right_pin_1 = 11
left_pin_1 = 12
GPIO.setup(right_pin_1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(left_pin_1, GPIO.OUT, initial=GPIO.HIGH)

# Servo 2
right_pin_2 = 15
left_pin_2 = 16
GPIO.setup(right_pin_2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(left_pin_2, GPIO.OUT, initial=GPIO.HIGH)


print("Interface to control 2 steppers and 2 servos")
print("Usage:\ncommand motor number")
print("Possible commands:\n")
print("Stepper control\n\ti: increase speed\n\tk: decrease speed\n\tf: go forward\n\tb: go backard")
print("Servo control\n\tr: turn right\n\tl: turn left\n\ts: stop turning")
print("Example motor: i1 d2\nExaple servo r2 s1")
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
        match (inpt):
            # Motor 1 logic
            case "i1":
                dc1 = change_dc(dc1, 10)
                print(dc1)
                pwm1.ChangeDutyCycle(dc1)
            case "k1":
                dc1 = change_dc(dc1, -10)
                print(dc1)
                pwm1.ChangeDutyCycle(dc1)
            case "b1":
                GPIO.output(dir1_pin, GPIO.LOW)
            case "f1":
                GPIO.output(dir1_pin, GPIO.HIGH)
            # Motor 2 logic
            case "i2":
                dc2 = change_dc(dc2, 10)
                print(dc2)
                pwm2.ChangeDutyCycle(dc2)
            case "k2":
                dc2 = change_dc(dc2, -10)
                print(dc2)
                pwm2.ChangeDutyCycle(dc2)
            case "b2":
                GPIO.output(dir2_pin, GPIO.LOW)
            case "f2":
                GPIO.output(dir2_pin, GPIO.HIGH)
            
            # Servo 1 logic
            case "s1":
                GPIO.output(right_pin_1, 1)
                GPIO.output(left_pin_1, 1)
            case "r1":
                GPIO.output(right_pin_1, 0)
                GPIO.output(left_pin_1, 1)
            case "l1":
                GPIO.output(right_pin_1, 1)
                GPIO.output(left_pin_1, 0)

            # Servo 2 logic
            case "s2":
                GPIO.output(right_pin_1, 1)
                GPIO.output(left_pin_1, 1)
            case "r2":
                GPIO.output(right_pin_2, 0)
                GPIO.output(left_pin_2, 1)
            case "l2":
                GPIO.output(right_pin_2, 1)
                GPIO.output(left_pin_2, 0)


except KeyboardInterrupt:
    print("Ctl C pressed - ending program")

pwm1.stop()                         # stop PWM
pwm2.stop()                         # stop PWM

GPIO.cleanup()                     # resets GPIO ports used back to 
