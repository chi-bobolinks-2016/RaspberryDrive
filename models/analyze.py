# Import image library necessary for file
import SimpleCV
import sys
from SimpleCV import Image

def check_blob_in_direct_path(image_path):

	image = Image(image_path)
	# grey = image.grayscale()

	instruction = "forward"
	array_bounds_possible_widths = [image.width / 4, image.width / 4 * 3]
	shapes_pic_attributes = image.size()

	shapes_pic_size = shapes_pic_attributes[0] * shapes_pic_attributes[1]
	# dist = img.colorDistance(SimpleCV.Color.Black).dilate(2)
	blobs = image.findBlobs()

	#check if the blob is in the middle 1/2 of screen and is too high
	for blob in blobs[:-1]:
		blob.draw(color=(255,0,0))
		if (blob.coordinates()[0] > array_bounds_possible_widths[0] and blob.coordinates()[0] < array_bounds_possible_widths[1]) and (blob.height() > image.height / 5 and blob.coordinates()[1] > image.height / 5 * 2):
			# print grey.height
			blob.draw(color=(255,0,0))
			instruction = "stop"

	return instruction

