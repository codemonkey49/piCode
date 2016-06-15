import unicornhat as UH
import time
#while True:
#    for y in range(8):
#        for x in range(8):
#            UH.set_pixel(x,y,random.randint(0,255),random.randint(0,255),random.randint(0,255))
#   UH.show()
#   time.sleep(0.1)

A=[0,0,0,1,0,0,0,1]
B=[1,0,0,1,0,0,0,0]
C=[0,0,0,1,0,0,0,1]
D=[0,0,0,1,0,0,0,0]
E=[0,0,0,1,0,0,0,0]
F=[0,0,0,1,0,0,0,0]
G=[0,0,0,1,0,0,0,0]
H=[0,0,0,0,1,0,0,0]


full=[H,G,F,E,D,C,B,A]

def setColor(full):
    for y in range (8):
        for x in range (8):
            if full[y][x]==1:
                UH.set_pixel(7-x,y,255,255,255)
    UH.show()
                
    time.sleep(5)

setColor(full)

        
    
    
