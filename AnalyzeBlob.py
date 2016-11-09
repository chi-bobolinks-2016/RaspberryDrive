import SimpleCV
import cv2
import time

class AnalyzeBlob(object):

	def __init__(self,img,blob):
		self.vertical_boundary = 0.45
		self.width_boundary = 0.4
		self.img = img
		self.blob = blob

	def isBlobBlocking(self):
		if (self.__heightBelowThreshold() && self.__widthSufficientToBlock()):
				return True

	def isBlobDetectedLeft(self):


	def isBlobDetectedRight(self):


	def __heightBelowThreshold(self):
		if (self.blob.maxY() > self.img.size()[1] * self.vertical_boundary):
			return True

	def __widthSufficientToBlock(self):
		if (self.blob.width() > self.img.size()[0] * self.width_boundary):
				return True

