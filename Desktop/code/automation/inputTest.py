from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m=PyMouse()
k=PyKeyboard()


x,y=m.position()
#print y
print x,y
m.move(790,304)
m.click(790,304)
k.type_string("edson@smith.net")
time.sleep(1)
m.move(784,345)
m.click(784,345)
k.type_string("gigglepig5")
time.sleep(1)
m.move(1054,325)
m.click(1054,325)

#m.click(x,y)
#time.sleep(5)
#m.click(648,98)
#k.type_string("Y")
#time.sleep(5)
#k.tap_key(k.enter_key)

#smithe65
#beaker1!
