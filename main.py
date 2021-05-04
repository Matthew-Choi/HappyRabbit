import random
import time
from ButtonController import *
from LEDController import *
from ServoController import *
from adafruit_servokit import ServoKit
# LED Controller for LED Strip to turn on/off certain colors
import board
import neopixel
import time

# Configure the setup
PIXEL_PIN = board.D18 # pin that is connected to the boar
ORDER = neopixel.RGB # Pixel color channel Order
NUM_PIXELS = 60 #number of pixels
pixels = neopixel.NeoPixel(PIXEL_PIN, 120)

#servos
kit = ServoKit(channels=16)


def main():
    setLeds()
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

def setLeds():
    # red
    pixels[0] = (255, 0, 0)
    pixels[1] = (255, 0, 0)
    pixels[2] = (255, 0, 0)
    pixels[3] = (255, 0, 0)
    pixels[4] = (255, 0, 0)
    pixels[5] = (255, 0, 0)
    pixels[6] = (255, 0, 0)
    pixels[7] = (255, 0, 0)
    pixels[8] = (255, 0, 0)
    pixels[9] = (255, 0, 0)

    # clear
    pixels[10] = (0, 0, 0)
    pixels[11] = (0, 0, 0)
    pixels[12] = (0, 0, 0)
    pixels[13] = (0, 0, 0)
    pixels[14] = (0, 0, 0)
    pixels[15] = (0, 0, 0)
    pixels[16] = (0, 0, 0)
    pixels[17] = (0, 0, 0)

    # green
    pixels[18] = (0, 255, 0)
    pixels[19] = (0, 255, 0)
    pixels[20] = (0, 255, 0)
    pixels[21] = (0, 255, 0)
    pixels[22] = (0, 255, 0)
    pixels[23] = (0, 255, 0)
    pixels[24] = (0, 255, 0)
    pixels[25] = (0, 255, 0)
    pixels[26] = (0, 255, 0)
    pixels[27] = (0, 255, 0)

    # clear
    pixels[28] = (0, 0, 0)
    pixels[29] = (0, 0, 0)
    pixels[30] = (0, 0, 0)
    pixels[31] = (0, 0, 0)
    pixels[32] = (0, 0, 0)
    pixels[33] = (0, 0, 0)
    pixels[34] = (0, 0, 0)
    pixels[35] = (0, 0, 0)

    # Blue
    pixels[36] = (0, 0, 255)
    pixels[37] = (0, 0, 255)
    pixels[38] = (0, 0, 255)
    pixels[39] = (0, 0, 255)
    pixels[40] = (0, 0, 255)
    pixels[41] = (0, 0, 255)
    pixels[42] = (0, 0, 255)
    pixels[43] = (0, 0, 255)
    pixels[44] = (0, 0, 255)
    pixels[45] = (0, 0, 255)


if __name__ == "__main__":
    main()
