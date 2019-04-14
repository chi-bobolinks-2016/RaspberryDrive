import RPi.GPIO as GPIO
from time import sleep

class PiCar(object):
		
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
        	self.pins = {'left'     : 11,
                	     'right'    : 18,
                	     'forward'  : 16,
                     	     'backward' : 12 }
        	for pin_number in self.pins.itervalues():
            		GPIO.setup(pin_number,GPIO.OUT)
		self.stop()


	def stop(self):
        	for pin_number in self.pins.itervalues():
             		GPIO.output(pin_number,0)

     	def go_forward(self,time):
        	self.stop()
         	GPIO.output(self.pins['forward'],1)
         	sleep(int(time))
         	self.stop()

	def go_backward(self,time):
        	self.stop()
         	GPIO.output(self.pins['backward'],1)
         	sleep(int(time))
         	self.stop()

     	def go_forward_right(self,time):
        	self.stop()
         	GPIO.output(self.pins['right'],1)
         	GPIO.output(self.pins['forward'],1)
         	sleep(int(time))
         	self.stop()

	def go_forward_left(self,time):
		self.stop()
         	GPIO.output(self.pins['left'],1)
         	GPIO.output(self.pins['forward'],1)
         	sleep(int(time))
        	self.stop()

	def go_backward_right(self,time):
         	self.stop()
         	GPIO.output(self.pins['right'],1)
         	GPIO.output(self.pins['backward'],1)
         	sleep(int(time))
         	self.stop()

	def go_backward_left(self,time):
         	self.stop()
         	GPIO.output(self.pins['left'],1)
         	GPIO.output(self.pins['backward'],1)
         	sleep(int(time))
         	self.stop()


picar = PiCar()

