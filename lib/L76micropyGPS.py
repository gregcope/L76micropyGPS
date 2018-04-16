from machine import Timer
import _thread
import gc
import binascii

# http://www.gpsinformation.org/dale/nmea.htm#GGA
# https://forum.pycom.io/topic/1626/pytrack-gps-api/12
class L76micropyGPS:

    GPS_I2CADDR = const(0x10)

    def __init__(self, my_gps, pytrack=None, sda='P22', scl='P21', timeout=None):
        if pytrack is not None:
            self.i2c = pytrack.i2c
        else:
            from machine import I2C
            self.i2c = I2C(0, mode=I2C.MASTER, pins=(sda, scl))

        self.chrono = Timer.Chrono()
        self.timeout = timeout
        self.timeout_status = True

        self.my_gps = my_gps

        # config GPS hints
        # https://forum.pycom.io/topic/2449/changing-the-gps-frequency-and-configuring-which-nmea-sentences-the-gps-posts/7
        # Stop logging to local flash of GPS
        #self.stoplog = "$PMTK185,1*23\r\n"
        #self.i2c.writeto(GPS_I2CADDR, self.stoplog)
        self.i2c.writeto(GPS_I2CADDR, "$PMTK185,1*23\r\n")
        # Use GPS, GONASS, GALILEO and GALILEO Full satellites
        #self.searchmode = "$PMTK353,1,1,1,1,0*2B\r\n"
        #self.i2c.writeto(GPS_I2CADDR, self.searchmode)
        self.i2c.writeto(GPS_I2CADDR, "$PMTK353,1,1,1,1,0*2B\r\n")

        # Do an empty write ...
        self.reg = bytearray(1)
        self.i2c.writeto(GPS_I2CADDR, self.reg)

        # start thread feeding microGPS
        _thread.start_new_thread(self.feedMicroGPS())

    def feedMicroGPS(self):
        print('Running feedGps_thread id: {}'.format(_thread.get_ident()))
        someNmeaData = b''
        while True:
            if self.timeout is not None and self.chrono.read() >= self.timeout:
                self.chrono.stop()
                chrono_timeout = self.chrono.read()
                self.chrono.reset()
                self.timeout_status = False
                debug_timeout = True
            if not self.timeout_status:
                gc.collect()
                break

            # get some NMEA data
            someNmeaData = self.i2c.readfrom(GPS_I2CADDR, 128)
            print(" feedGps_thread - gpsChars recieved : {}".format(len(someNmeaData)))

            # Pass NMEA data to micropyGPS object
            for x in someNmeaData:
                self.my_gps.update(str(x))

            # tidy
            gc.collect()
        self.timeout_status = True

        if debug and debug_timeout:
            print('GPS timed out after %f seconds' % (chrono_timeout))
