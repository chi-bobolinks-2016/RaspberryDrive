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
	#os.unlink('greg.jpg')
	img = cam.capture('gregTest.jpg')
	time.sleep(.25)
	#oc.rename('gregTemp.jpg', 'greg.jpg')
	x +=1
exit()
