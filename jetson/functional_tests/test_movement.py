import Jetson.GPIO as GPIO
import time


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

GPIO.setmode(GPIO.BOARD)
left_motor = Motor(33, 31, invert=True)
right_motor = Motor(32, 35)



# # Move forward
# left_motor.set_speed(20)
# right_motor.set_speed(20)
# time.sleep(4)

# # Turn
# left_motor.set_speed(20)
# right_motor.set_speed(50)
# time.sleep(2)

# # Move backrward
# left_motor.set_speed(-10)
# right_motor.set_speed(-10)
# time.sleep(2)

left_motor.set_speed(0)
right_motor.set_speed(20)
time.sleep(4)



left_motor.set_speed(0)
right_motor.set_speed(0)



# pwm1.stop()
# pwm2.stop()
del(left_motor)
del(right_motor)
GPIO.cleanup() 