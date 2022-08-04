#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while True:
	tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
	cpu_temp_raw = tmpFile.read()
	tmpFile.close()
	cpu_temp = round(float(cpu_temp_raw)/1000, 1)

	if cpu_temp>=60:
		GPIO.output(11,1)
		print "True"

	if cpu_temp<40:
		GPIO.output(11,0)
		print "False"

	time.sleep(5)
