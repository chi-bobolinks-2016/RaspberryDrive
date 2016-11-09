import SimpleCV
import cv2
import time
from AnalyzeBlob import *

class AnalyzeImage(object):

  def __init__(self, image):
    self.default_command = "stop"
    self.scvImg = SimpleCV.Image(image)
    self.segmented_black_white = scvImg.stretch(160,161)
    self.black_white_blobs = segmented_black_white.findBlobs(minsize=100)

  def runBlobFinder(self):
    if (self.black_white_blobs and (len(self.black_white_blobs) > 0)):
      return self.analyzeBlobs()
    return False
  # print x
	# print blob

  def analyzeBlobs(img,blobs):
    for blob in self.black_white_blobs:
      analyzed_blob = AnalyzeBlob(self.scvImg,blob)
      if analyzed_blob.isBlobBlocking():
        return "Stop"
      if analyzed_blob.isBlobDetectedLeft()
        return ""

