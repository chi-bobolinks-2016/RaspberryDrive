import SimpleCV
import cv2
import time

class AnalyzeBlob(object):

	def __init__(self,img,blob):
		self.vertical_boundary = 0.3
		self.width_boundary = 0.4
		self.img = img
		self.blob = blob
		self.angle_to_turn = 30

	def isBlobBlocking(self):
		if (self.__heightBelowThreshold() and self.__widthSufficientToBlock()):
				return True

	def isBlobDetectedOnLeft(self):
		if (self.__anglingFromLeft() and self.__largeObjectStartingNearLeft()):
			return True

	def isBlobDetectedOnRight(self):
		if (self.__anglingFromRight() and self.__largeObjectStartingNearRight()):
			return True

	def __anglingFromRight(self):
		return self.blob.angle() < self.angle_to_turn

	def __largeObjectStartingNearRight(self):
		return (self.blob.maxX() > self.img.size()[0] * 0.95) and (self.blob.width() > self.img.size()[0] * 0.8) and (self.blob.maxY() > self.img.size()[1] * 0.3)

	def isBlobBlockingMoreRight(self):
		self.blob.angle() > 0

	def __anglingFromLeft(self):
		print self.blob.angle()
		return self.blob.angle() > 90 - self.angle_to_turn

	def __largeObjectStartingNearLeft(self):
		return (self.blob.maxX() < self.img.size()[0] * 0.05) and (self.blob.width() > self.img.size()[0] * 0.8) and (self.blob.maxY() > self.img.size()[1] * 0.3)

	def __heightBelowThreshold(self):
		return self.blob.maxY() > self.img.size()[1] * self.vertical_boundary

	def __widthSufficientToBlock(self):
		print self.blob.width() > self.img.size()[0] * self.width_boundary
		return self.blob.width() > self.img.size()[0] * self.width_boundary


