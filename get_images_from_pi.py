import os
from PIL import Image

def get_image_x_times(times):
	count = 0
	while count < times:
		#replace sleep with the amount of time needed to sleep in between getting pictures.
		time.sleep(0.5)
		count += 1

def get_image():
	os.system('scp pi@192.168.2.5:Desktop/gregTest.jpg gregTest.jpg')
	return
	#if on a new computer and the pi address isn't connecting right away, need to create a key.  Use the following website to do so
	#https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md

def valid_image(path):
	try:
		Image.open(path)
	except IOError:
		return False
	return True
