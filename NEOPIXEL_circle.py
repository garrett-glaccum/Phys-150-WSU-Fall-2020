import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = .15

i=255;
while True:
    cp.pixels.fill((50,50,50))
    time.sleep(1)
    while (i>0):
        i-=51
        time.sleep(0.06)
        cp.pixels[0] = (255-i, 0, 0)
        time.sleep(0.06)
        cp.pixels[1] = (255-i, 255-i, 0)
        time.sleep(0.06)
        cp.pixels[2] = (255-i, 255-i, 255-i)
        time.sleep(0.06)
        cp.pixels[3] = (255-i, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[4] = (0, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[5] = (0, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[6] = (255-i, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[7] = (255-i, 255-i, 255-i)
        time.sleep(0.06)
        cp.pixels[8] = (255-i, 255-i, 0)
        time.sleep(0.06)
        cp.pixels[9] = (255-i, 0, 0)
        time.sleep(0.06)
    while (i<255):
        i+=51
        time.sleep(0.06)
        cp.pixels[9] = (255-i, 0, 0)
        time.sleep(0.06)
        cp.pixels[8] = (255-i, 255-i, 0)
        time.sleep(0.06)
        cp.pixels[7] = (255-i, 255-i, 255-i)
        time.sleep(0.06)
        cp.pixels[6] = (255-i, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[5] = (0, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[4] = (0, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[3] = (255-i, 0, 255-i)
        time.sleep(0.06)
        cp.pixels[2] = (255-i, 255-i, 255-i)
        time.sleep(0.06)
        cp.pixels[1] = (255-i, 255-i, 0)
        time.sleep(0.06)
        cp.pixels[0] = (255-i, 0, 0)
        time.sleep(0.06)
