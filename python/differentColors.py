import board
import neopixel
from time import sleep
import random

##Set up light board
numLights=50
pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
##Turn on one light, blue
pixels[1]=(0,0,225)
pixels.show()
sleep(1)
##Turn on one light, green
pixels[1]=(0,225,0)
pixels.show()
sleep(1)
##Turn on one light, red
pixels[1]=(225,0,0)
pixels.show()
sleep(1)
##Turn on one light, white
pixels[1]=(225,220,220)
pixels.show()
sleep(1)
##Turn on one light, yellow
pixels[1]=(200,200,0)
pixels.show()
sleep(1)
##Turn on one light, purple
pixels[1]=(200,0,200)
pixels.show()
sleep(1)

