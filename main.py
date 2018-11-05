import math
import time
import utime
from L76micropyGPS import L76micropyGPS
from micropyGPS import MicropyGPS
from pytrack import Pytrack
import gc

#
# You will need the following lines
# The print statements can be removed - they are just here to debug
#

# enable GC
gc.enable()

print("Free Mem: {}".format(gc.mem_free()))

# Start GPS, you need this line
py = Pytrack()

print("Free Mem post pytrack instantiation: {}".format(gc.mem_free()))

# Start a microGPS object, you need this line
my_gps = MicropyGPS(location_formatting='dd')

print("Free Mem post my_gps instantiation: {}".format(gc.mem_free()))

# Start the L76micropyGPS object, you need this line
L76micropyGPS = L76micropyGPS(my_gps, py)

# Start the thread, you need this line
gpsThread = L76micropyGPS.startGPSThread()

print("startGPSThread thread id is: {}".format(gpsThread))

#
# Do what you like now, examples below
# at some point you should want to read GPS/GNS data
# you need none of these lines, but I would assume
# at least one line doing something with my_gps object ...
# 

#start rtc
rtc = machine.RTC()
print("Free Mem post rtc instantiation: {}".format(gc.mem_free()))
start = utime.ticks_ms()
print("RTC time : {}".format(rtc.now()))
print('Aquiring GPS signal ', end='')
#try to get gps date to config rtc

#
# Just and example while thread to spit out
# GPS/GNS data to the console/uart
#
while (True):
    print("my_gps.parsed_sentences: {}".format(my_gps.parsed_sentences))
    print("my_gps.satellites_in_use: {}".format(my_gps.satellites_in_use))
    print("my_gps.date: {}".format(my_gps.date))
    print("my_gps.timestamp: {}".format(my_gps.timestamp))
    print("my_gps.hdop: {}".format(my_gps.hdop))
    print("Free Mem: {}".format(gc.mem_free()))
    time.sleep(1)

# switch off heartbeat LED
#pycom.heartbeat(False)
#print('Going to kipp 2 secs in 1 sec')
#time.sleep(1)
#py.setup_sleep(2)
#py.go_to_sleep(gps=True)
