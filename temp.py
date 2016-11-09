from analyzeimage import *
import os
import connect

connection = connect.new_connection()
new_image = AnalyzeImage(os.getcwd() + '/images/testAngle4.jpg',connection)
print new_image.runBlobFinder()
