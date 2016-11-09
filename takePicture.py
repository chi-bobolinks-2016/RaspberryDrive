import picamera as p
import os
import time

os.chdir('/home/pi/Desktop')

cam = p.PiCamera()
cam.resolution = (320,240)
cam.hflip = True
cam.vflip = True

x = 0
while x < 50:
	img = cam.capture('tempGregTest.jpg')
	os.unlink('gregTest.jpg')
	os.rename('tempGregTest.jpg','gregTest.jpg')
	time.sleep(.25)
	x +=1

exit()
