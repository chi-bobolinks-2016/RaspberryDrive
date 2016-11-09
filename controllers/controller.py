import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
import AnalyzeBlob
import AnalyzeImage
from AnalyzeImage import *
from AnalyzeBlob import *
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation,send_end_connection
from start_camera import start_camera
from start_server import start_server
import threading

def start_server_thread():
	server_thread = threading.Thread(target=start_server)
	server_thread.start()

def start_camera_thread():
	camera_thread = threading.Thread(target=start_camera)
	camera_thread.start()

def start_all():
  start_server_thread()
  start_camera_thread()
  sleep(7)
  s = new_connection()
  return s
  #start the server listening on contr pi
  #start the camera taking pictures on camera pi
  # Sleep to make sure server connects
  #start the server connection on this current server

def end_all(server):
  send_end_connection(server)
  server.close()
  #End-all
  #Camera exits automatically automatically
  #Close the Server Connection on the Pi-Controller End
  #Kill the server listening process

def run(server):
  count = 0
  while (count < 20):
    instruction = "forward"
    #retrieve image.
    get_image(count)
    if valid_image(os.getcwd() + "/gregTest.jpg"):
      #Blog Detection
      analyzed_image = AnalyzeImage(os.getcwd() + "/gregTest.jpg")
      command = analyzed_image.runBlobFinder()
      if (in_way == True):
        instruction = "stop"
      #send instruction over server
      send_command(server, instruction, "0.5")
      #confirmation that instruction was received
      receive_confirmation(server)
      print instruction
    count += 1

server = start_all()
run(server)
end_all(server)
#exit out of controller
exit()
