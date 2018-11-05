# L76micropyGPS
A pytrack L76 class that feeds a micropyGPS object POC

Intro
================
* Assumes USB connected Pytrack/Pycom modules (e.g Gpy) to print messages to the console
* Uses the fabulous MicroGPS module from https://github.com/inmcm/micropyGPS
* Uses some Pytrack/PySense code from 
https://github.com/pycom/pycom-libraries/blob/master/pytrack/lib/pytrack.py

Usage
=================
1. Checkout the repo
2. Flash your device
3. Read the ``setup.py`` and ``main.py``` for examples

Own usage
=================
Use the ``main.py`` code as an example

NOTES
=================
*Presently the ``pycoproc`` code assumes an ``i2c`` ID of ``0`` here; https://github.com/pycom/pycom-libraries/blob/master/lib/pycoproc/pycoproc.py#L78


Todo
=================
* Add something to stop thread
