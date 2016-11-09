from connect import *

class CarManeuvers(object):

  def __init__(self,connection):
    self.connection = connection

  def forward(self):
    print "executing forward"
    send_command(self.connection, "forward", "0.5")

  def right(self):
    print "executing right"
    send_command(self.connection, "right", "0.5")

  def left(self):
    print "executing left"
    send_command(self.connection, "left", "0.5")

  def back_up_then_right(self):
    print "executing back up and drive right"
    send_command(self.connection, "backwards", "0.75")
    send_command(self.connection, "right", "0.5")

  def back_up_then_left(self):
    print "executing back up and drive left"
    send_command(self.connection, "backwards", "0.75")
    send_command(self.connection, "left", "0.5")

