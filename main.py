import random
import time
from ButtonController import *
from LEDController import *
from ServoController import *
from adafruit_servokit import ServoKit

#servos
kit = ServoKit(channels=16)

def main():
    while 1: 
        random.seed(time.time())
        option = random.randint(1, 3)

        # Turn on the corresponding LED
        print("hello")
        if option == 1:
            # Turn on red LED
            blink_led()
            print("Red (1)")
        elif option == 2:
            # Turn on green LED
            blink_led()
            print("Green (2)")
        elif option == 3:
            # Turn on blue LED
            blink_led()
            print("Blue (3)")

        # need code to timeout after x seconds
        # can be based off difficulty, or can utilize learning
        # github examples (may only work on pi but that is ok)
        # https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
        # https://gist.github.com/atupal/5865237

        get_button()
        choice = input()

        if int(choice) == option:
            # activate servo control to release treat/reward
            # run_servo()
            kit.servo[4].angle = 180
            time.sleep(0.25)
            kit.servo[4].angle = 0
            # send call to AWS to store data
            print("correct!")
            print("")
        else:
            # Negative Feedback?
            print("incorrect!")
            print("")


if __name__ == "__main__":
    main()
