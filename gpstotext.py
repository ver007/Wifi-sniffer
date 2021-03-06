#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import math
import os
from gps import *
from time import *
import time
import threading
import pickle
import time
 
gpsd = None #seting the global variable
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  lat = 0
  lon = 0
  start_time = time.time()
  try:
    gpsp.start() # start it up
    
    while True:
      theTime = int(round(time.time()-start_time,0))
      if math.isnan(gpsd.fix.latitude) or math.isnan(gpsd.fix.longitude):
        cords = [lat,lon,theTime]
      else:
       lat,lon = gpsd.fix.latitude,gpsd.fix.longitude
      cords = [lat,lon,theTime]
      pickle.dump(cords,open("gps.p","wb"))
      time.sleep(1) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
