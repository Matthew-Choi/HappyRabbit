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
import digitalio

# Configure the setup for LED
PIXEL_PIN = board.D18 # pin that is connected to the boar
ORDER = neopixel.RGB # Pixel color channel Order
NUM_PIXELS = 60 #number of pixels
pixels = neopixel.NeoPixel(PIXEL_PIN, 60, brightness=0.2)

# servos
kit = ServoKit(channels=16)

# button
blue_button = digitalio.DigitalInOut(board.D4)
blue_button.direction = digitalio.Direction.INPUT

def main():
    while 1:
        turnOffAll()
        random.seed(time.time())
        option = random.randint(1, 3)

        # Turn on the corresponding LED
        print("hello")
        if option == 1:
            # Turn on red LED
            setRed()
            print("Red (1)")
        elif option == 2:
            # Turn on green LED
            setGreen()
            print("Green (2)")
        elif option == 3:
            # Turn on blue LED
            setBlue()
            print("Blue (3)")

        # need code to timeout after x seconds
        # can be based off difficulty, or can utilize learning
        # github examples (may only work on pi but that is ok)
        # https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
        # https://gist.github.com/atupal/5865237

        choice = get_button_input()

        # choice = input()
        if choice == "e":
            turnOffAll()
            break
        elif int(choice) == option:
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

        time.sleep(3)
    turnOffAll()

def get_button_input():
    bIn = 0
    while bIn == 0:
        if blue_button.value:
            bIn = 3
    return bIn

def setLedsALL():
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

def turnOffAll():
    pixels.fill((0, 0, 0))

def setRed():
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

def setBlue():
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

def setGreen():
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


if __name__ == "__main__":
    main()
