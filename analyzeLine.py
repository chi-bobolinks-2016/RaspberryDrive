import SimpleCV
import cv2
import time


def findBlockingBlobs(img,blobs):
	for blob in blobs:
		if blockingBlob(img,blob):
			return True
		return False

def blockingBlob(img,blob):
	if heightBelowThreshold(img,blob):
		if lengthSufficientToBlock(img,blob):
			return True

def heightBelowThreshold(img,blob):
	if (blob.maxY() > img.size()[1] * 0.4):
		return True

def lengthSufficientToBlock(img,blob):
	if (blob.width() > img.size()[0] * 0.55):
			return True

