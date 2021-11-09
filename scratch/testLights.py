import board
import neopixel
from time import sleep
import random


numLights=50
pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
pixels.fill((0,0,0))
sleep(1)
while True:
    red = random.randrange(0,255)
    blue = random.randrange(0,255)
    green = random.randrange(0,255)
    print("red = ", red, "green = ", green, "blue=", blue)
    for p in range(0,numLights):
        pixels[p]=(red,green,blue)
        sleep(0.05)
        pixels.show()
            
    for p in range(numLights-1,0,-1):
        pixels[p]=(0,0,0)
        sleep(0.05)
        pixels.show()
