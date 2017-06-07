#Area Calculator
#Area Calculator

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Calculator is Starting UP"

print '%s/%s/%s %s:%s' % (now.month,now.day,  now.year, now.hour, now.minute)

sleep(1)
hint ='Don\'t forget to include the correct units! \nExiting...'

option= raw_input("Enter C for Circle or T for Triangle:").upper()

if (option == 'C'):
  radius = float(raw_input("radius"))
  area = pi*(radius**2)
  print "The Pie is Baking"
  sleep(1)
  print (round(area,2))
elif (option == 'T'):
  base = float(raw_input("base"))
  height = float(raw_input("height"))
  area = base*height/2
  print "Uni Bi Tri"
  sleep(1)
  print (round(area,2))
else:
  print 'Incorrect Input Exiting From Program'