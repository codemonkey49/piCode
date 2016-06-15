import unicornhat as UH
import time
import random
#while True:
#    for y in range(8):
#        for x in range(8):
#            UH.set_pixel(x,y,random.randint(0,255),random.randint(0,255),random.randint(0,255))
#   UH.show()
#   time.sleep(0.1)



def setColor(full):
    for y in range (8):
        for x in range (8):
            if full[y][x]==100:#white, alive
                UH.set_pixel(7-x,y,255,255,255)
            elif full [y][x]==1:#green, will come to life
                UH.set_pixel(7-x,y,0,255,0)
            elif full[y][x]==101:#red, will die
                UH.set_pixel(7-x,y,255,0,0)
            elif full[y][x]==0:#nothing
                UH.set_pixel(7-x,y,0,0,0)
                

    UH.show()

def logic(full):
    for y in range (8):
        for x in range (8):
                liveCount=0
                if y !=7:
                    liveCount+=full[y+1][x]
                if x != 7 and y!=7:
                    liveCount+=full[y+1][x+1]
                if x !=7:
                    liveCount+=full[y][x+1]
                if x !=7 and y !=0:
                    liveCount+=full[y-1][x+1]
                if y!=0:
                    liveCount+=full[y-1][x]
                if y !=0 and x!=0:
                    liveCount+=full[y-1][x-1]
                if x !=0:
                    liveCount+=full[y][x-1]
                if x !=0 and y !=7:
                    liveCount+=full[y+1][x-1]

                    
                if liveCount >= 300 and liveCount<=350 and full[y][x]==0:
                    full[y][x]=1

                if full[y][x]==100 and liveCount<200:
                    full[y][x]=101

                if full[y][x]==100 and liveCount>400:
                    full[y][x]=101

                    
    #print full[5]
    setColor(full)
    return full



def main():
    while True:
        A=[0,0,0,0,0,0,0,0]
        B=[0,0,0,0,0,0,0,0]
        C=[0,0,0,0,0,0,0,0]
        D=[0,0,0,0,0,0,0,0]
        E=[0,0,0,0,0,0,0,0]
        F=[0,0,0,0,0,0,0,0]
        G=[0,0,0,0,0,0,0,0]
        H=[0,0,0,0,0,0,0,0]
        full=[H,G,F,E,D,C,B,A]
        for x in range (7):
            for y in range (7):
                if (random.randint(0,1)):
                    full[x][y]=100
        print full
        
        i=0
        while i<25:
            full=logic(full)
            #x=raw_input()
            time.sleep(1)
            for y in range (8):
                for x in range (8):
                    if full[y][x]==101:
                        full[y][x]=0
                    if full [y][x]==1:
                        full[y][x]=100
            i+=1

main()
                
    
    
