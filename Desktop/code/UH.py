import unicornhat as UH
import time
import random
while True:
    for y in range(8):
        for x in range(8):
            UH.set_pixel(x,y,random.randint(0,255),random.randint(0,255),random.randint(0,255))
    UH.show()
    time.sleep(0.1)

