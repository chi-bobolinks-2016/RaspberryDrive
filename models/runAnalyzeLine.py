import SimpleCV
import cv2
import time
from analyzeLine import *

def runAnalyzeLines(image):
	scvImg = SimpleCV(image)
	segmented = scvImg.stretch(160,161)
	blob = segmented.findBlobs(minsize=100)

	# print x
	# print blob
	return findBlockingBlobs(scvImg,blob)