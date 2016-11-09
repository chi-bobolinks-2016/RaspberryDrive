import SimpleCV
import cv2
import time
from analyzeblob import *
from car_maneuvers import *
from PIL import Image

class AnalyzeImage(object):

  def __init__(self, image,connection):
    self.default_command = "stop"
    self.scvImg = SimpleCV.Image(image)
    self.segmented_black_white = self.scvImg.stretch(160,161)
    self.black_white_blobs = self.segmented_black_white.findBlobs(minsize=100)
    self.car = CarManeuvers(connection)

  def runBlobFinder(self):
    if (self.black_white_blobs and (len(self.black_white_blobs) > 0)):
      self.analyzeBlobs()
    else:
      self.car.forward()
  # print x
	# print blob

  def analyzeBlobs(self):
    blobs = self.scvImg.findBlobs(minsize = 100)
    # if blobs:
    #   for blob in blobs:
    #     if blob.area() > 100:
    #       blob.draw(color=(128,0,0))
    #   self.scvImg.show()
    #   self.scvImg.show()
    #   time.sleep(2)
    #check if blocked
    for blob in self.black_white_blobs:
      print blob
      analyzed_blob = AnalyzeBlob(self.scvImg,blob)

      if analyzed_blob.isBlobBlocking():
        print "true"
        if analyzed_blob.isBlobBlockingMoreRight():
          self.car.back_up_and_then_drive_left()
        else:
          self.car.back_up_and_then_drive_right()
        return

      elif analyzed_blob.isBlobDetectedOnRight():
        # if analyzed_blob.blockedOnRight():
        self.car.left()
        return
      elif analyzed_blob.isBlobDetectedOnLeft():
        self.car.right()
        return
    #otherwise go forward
    self.car.forward()

#  detect blobs
#  if blobs
#    check left and check rightt
#     is blocking?
#         back up
#       else
#         turn (in correct direction)
