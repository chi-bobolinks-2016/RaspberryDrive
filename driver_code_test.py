import SimpleCV
from SimpleCV import Image
import cv2
import time
from start_camera import start_camera
import threading

camera_thread = threading.Thread(target=start_camera)
camera_thread.start()
from get_images_from_pi import get_image, valid_image

count = 0
while (count < 10):
  get_image(count)
  count += 1

exit()

# image = Image('images/9.jpg')
# # p = image.getPalette()
# # rgb = PIL.ImageColor.getrgb("blue")
# # print rgb
# blobs = image.findBlobs(threshval=(0,0,255))
# # blobs = image.findBlobsFromPalette( (p[0],p[1],p[2]) )
# # blobs = image.findBlobsFromHueHistogram((0,0,50,50))
# if blobs:
#   for blob in blobs:
#     print "got a blob"
#     blob.draw(color=(0, 128, 0))
# image.show()
# image.show()
# time.sleep(4)






