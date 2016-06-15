import picamera
from time import sleep
camera=picamera.PiCamera()
camera.vflip = True

#camera.capture("image.jpg")

camera.start_preview()

