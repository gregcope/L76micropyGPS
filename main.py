import math
import time
import utime
from L76micropyGPS import L76micropyGPS
from micropyGPS import MicropyGPS
from pytrack import Pytrack
import gc

# enable GC
gc.enable()

print("Free Mem: {}".format(gc.mem_free()))

#Start GPS
py = Pytrack()
print("Free Mem post pytrack instantiation: {}".format(gc.mem_free()))

my_gps = MicropyGPS()
print("Free Mem post my_gps instantiation: {}".format(gc.mem_free()))

L76micropyGPS = L76micropyGPS(my_gps, py)

gpsThread = L76micropyGPS.startGPSThread()
print("startGPSThread thread id is: {}".format(gpsThread))

#start rtc
rtc = machine.RTC()
print("Free Mem post rtc instantiation: {}".format(gc.mem_free()))
start = utime.ticks_ms()
print("RTC time : {}".format(rtc.now()))
print('Aquiring GPS signal ', end='')
#try to get gps date to config rtc

while (True):
    print("my_gps.parsed_sentences: {}".format(my_gps.parsed_sentences))
    print("my_gps.satellites_in_use: {}".format(my_gps.satellites_in_use))
    time.sleep(2)

# switch off heartbeat LED
#pycom.heartbeat(False)
#print('Going to kipp 2 secs in 1 sec')
#time.sleep(1)
#py.setup_sleep(2)
#py.go_to_sleep(gps=True)
