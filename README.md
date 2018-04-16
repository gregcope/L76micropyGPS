# L76micropyGPS
A pytrack L76 class that feeds a micropyGPS object POC

Usage
================
* Assumes USB connected Pytrack/Pycom modules (e.g Gpy)
* Uses the fabulous MicroGPS module from https://github.com/inmcm/micropyGPS

Issues
=================
* thread starts, feeds GPS, but does not go into the background for main thread to run :-(
