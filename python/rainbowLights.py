import board
import neopixel
from time import sleep
import random

numLights=50
pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
pixels.fill((0,0,0))

def wheel(pos): ##Funtion that makes each light a different rainbow color
    if pos<0 or pos > 255:
        r= g= b=0
    elif pos<85:
        r= int(pos*3)
        g= int(255-pos*3)
        b=0
    elif pos<170:
        pos -=85
        r= int(255 -pos*3)
        g=0
        b=int(pos*3)
    else:
        pos-= 170
        r=0
        g=int(pos*3)
        b=int(255-pos*3)
    return (r,g,b)

       
pixels.fill((0,0,0))

while True:
    for p in range(0,numLights): ##look at all of our lights
        pixel_index = (p*256 // numLights) ##make the correct number of lights
        pixels[p] = wheel(pixel_index & 255) ##give the light a rainbow color
        sleep(0.05) ##how long before next light is filled in
    pixels.show()##show the color
       
    for p in range(numLights-1,0,-1):
        pixels[p]=(0,0,0)
        sleep(0.05)
        pixels.show()
       
   
    ##turns lights on and off 5 at a time
    for p in range(0,numLights,5): ##look at all of our lights
        pixel_index = (p*256 // numLights) ##make the correct number of lights
        pixels[p] = wheel(pixel_index & 255) ##give the light a rainbow color
        pixels[p+1] = wheel(pixel_index & 255)
        pixels[p+2] = wheel(pixel_index & 255)
        pixels[p+3] = wheel(pixel_index & 255)
        pixels[p+4] = wheel(pixel_index & 255)
        sleep(0.05) ##how long before next light is filled in
    pixels.show()##show the color
   
    for p in range(numLights-1,0,-5):
        pixels[p]=(0,0,0)
        pixels[p-1] = (0,0,0)
        pixels[p-2] = (0,0,0)
        pixels[p-3] = (0,0,0)
        pixels[p-4] = (0,0,0)
        sleep(0.05)
        pixels.show()
