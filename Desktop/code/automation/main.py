from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import os
from PIL import Image
m=PyMouse()
k=PyKeyboard()


def screenshot(name):
    os.system("scrot "+name+".png")
#screenshot("checkcheck")
#print "done"
def fullCompare(image1,image2):
    im1=Image.open(image1)
    im2=Image.open(image2)
    width,height=im1.size
    print(width,height)

    for x in range (0,width,width/100):
        for y in range (0,height,height/100):
            if im1.getpixel((x,y)) != im2.getpixel((x,y)):
                print ("fuck")
            #m.move(x,y)
#fullCompare("login.png","login.png")
print "done"   
def checkPointSelect():
    while True:
        x,y=m.position()
        

#x,y=m.position()
#print y
#print x,y
#m.move(790,304)
#m.click(790,304)
#k.type_string("edson@smith.net")
#time.sleep(1)
#m.move(784,345)
#m.click(784,345)
#k.type_string("gigglepig5")
#time.sleep(1)
#m.move(1054,325)
#m.click(1054,325)

#m.click(x,y)
#time.sleep(5)
#m.click(648,98)
#k.type_string("Y")
#time.sleep(5)
#k.tap_key(k.enter_key)

#smithe65
#beaker1!
