# LED Controller for LED Strip to turn on/off certain colors
import board
import neopixel
import time

# Configure the setup
PIXEL_PIN = board.D18 # pin that is connected to the boar
ORDER = neopixel.RGB # Pixel color channel Order
NUM_PIXELS = 60 #number of pixels
pixels = neopixel.NeoPixel(PIXEL_PIN, 120)

#red
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

#clear
pixels[10] = (0, 0, 0)
pixels[11] = (0, 0, 0)
pixels[12] = (0, 0, 0)
pixels[13] = (0, 0, 0)
pixels[14] = (0, 0, 0)
pixels[15] = (0, 0, 0)
pixels[16] = (0, 0, 0)
pixels[17] = (0, 0, 0)

#green
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

#clear
pixels[28] = (0, 0, 0)
pixels[29] = (0, 0, 0)
pixels[30] = (0, 0, 0)
pixels[31] = (0, 0, 0)
pixels[32] = (0, 0, 0)
pixels[33] = (0, 0, 0)
pixels[34] = (0, 0, 0)
pixels[35] = (0, 0, 0)

#Blue
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


def blink_led():
    print("LED Blinking")
