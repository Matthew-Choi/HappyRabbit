# Servo Controller Code
import time
from adafruit_servokit import ServoKit

def run_servo():
    kit = ServoKit(channels=16)
    kit.servo(4).angle = 180
    time.sleep(1) 
    kit.servo(4).angle = 0
    print("Servos Running")
