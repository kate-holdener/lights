import board
import neopixel
from time import sleep
import random

##Set up light board
numLights=50
pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
##Turn on one light
pixels[1]=(0,0,225)
pixels.show()

