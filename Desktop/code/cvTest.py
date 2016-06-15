from SimpleCV import *

cam=Camera()

while True:
    img=cam.getImage()
    green=img.colorDistance(Color.GREEN)
    img=img-green
    blob=img.findBlobs()
    blob.show()
