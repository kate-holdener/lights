import board
import neopixel
from time import sleep
import random

##Set up light board
numLights=50
pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
##Turn on many lights
for p in range(0,25):
        pixels[p]=(50,150,150)
pixels.show()
sleep(1)
##rest lights
pixels.fill((0,0,0))
sleep(1)
##Turn on all lights
pixels.fill((100,200,50))
pixels.show()