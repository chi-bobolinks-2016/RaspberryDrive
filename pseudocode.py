def driveforward(time):
  FOR each second in time
    goforward(1)
    IF isblocked?()
      return false
    END
  return true

def drivebackward(time):
  FOR each second in time
    gobackward(1)
    IF isblocked?()
      return false
    END
  return true

def isblocked?():
  IF checkcamera() && checkproximity()
    return true
  ELSE
    return false
  END

def goforward(time):
  FOR the length of time
    sendgoforwardsignaltocar()
     updatestraightcoordinates(time,"forward")
  return ;

def gobackward(time):
  FOR the length of time
    sendgobackwardsignaltocar()
    updatestraightcoordinates(time,"backward")
  return

def goforwardright(time):
  FOR the length of time
    sendgobackwardsignaltocar()
    sendgorightsignaltocar()
  return

def goforwardleft(time):
  FOR the length of time
    sendgobackwardsignaltocar()
    sendgorightsignaltocar()
  return

def maneuverright(backuptime,rightime):
  gobackward(backuptime)
  goright(righttime)
  return

def checkcamera():
  image = getimage()
  parseimage(image)
  return

def checkproximity():
  proximity = getproximitysignal()
  parseproximitysignal(image)
  return


def initialize(target_x, target_y):
#   carspeed = TBD
#   createcoordinates(0,0,90)
#   settargets(target_x,target_y)
#   return;

# def createcoordinates(initial_x,initial_y,initial_heading):
#   x = initial_x
#   y = initial_y
#   heading = initial_heading
#   return;

# def settargets(target_x,target_y):
#   final_x = target_x
#   final_y = target_y
#   return;

# def directiontotarget():
#   return math.degrees(math.atan((final_y - y)/(final_x - x)))

# def go():
#   orientdirection()
#   drivetotarget
#   return ;

# def orientdirection
#   if

# def updatestraightcoordinates(time,direction):
#   sphericalheading = heading * math.pi / 180
#   IF direction == "forward"
#     x = x + time * carspeed * math.cos(sphericalheading)
#     y = y + time * carspeed * math.sin(sphericalheading)
#   ELSE
#     x = x - time * carspeed * math.cos(sphericalheading)
#     y = y - time * carspeed * math.sin(sphericalheading)
#   END
#   return

# def updateturncoordinates(time,turningdirection):
#   sphericalheading = math.radians(heading)
#   FOR each 10th of a second in time
#     IF turningdirection == "right"
#       sphericalheading = sphericalheading - directionchangepertime
#     ELSE
#       sphericalheading = sphericalheading + directionchangepertime
#     END
#     x = x + time * carspeed * math.cos(sphericalheading)
#     y = y + time * carspeed * math.sin(sphericalheading)
#   return