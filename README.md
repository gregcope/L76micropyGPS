# L76micropyGPS
A pytrack L76 class that feeds a micropyGPS object POC

Intro
================
* Assumes USB connected Pytrack/Pycom modules (e.g Gpy) to print messages to the console/uart.
* Uses the fabulous MicroGPS module from https://github.com/inmcm/micropyGPS
* Uses some Pytrack/PySense code from 
https://github.com/pycom/pycom-libraries/blob/master/pytrack/lib/pytrack.py

Usage
=================
1. Checkout the repo
2. Flash your device
3. Read the ``boot.py`` and ``main.py`` for examples.  ``boot.py`` does very little bar start a timer for testing and the uart.

Own usage
=================
Use the ``main.py`` code as an example.  The ``print`` statements can be removed as they are there for memory / displaying to console.

NOTES
=================
*Presently the ``pycoproc`` code assumes an ``i2c`` ID of ``0`` here; https://github.com/pycom/pycom-libraries/blob/master/lib/pycoproc/pycoproc.py#L78


Todo
=================
* Add something to stop thread
