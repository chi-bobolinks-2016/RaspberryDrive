import SimpleCV
import cv2
import time
from analyzeLine import *

def runAnalyzeLines(image):
  scvImg = SimpleCV.Image(image)
  segmented = scvImg.stretch(160,161)
  blobs = segmented.findBlobs(minsize=100)
  if (blobs and (len(blobs) > 0)):
    return findBlockingBlobs(scvImg,blobs)
  return False
  # print x
	# print blob
