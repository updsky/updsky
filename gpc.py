#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:

	GPIO.output(11,1)
	print "True"

	time.sleep(5)

	GPIO.output(11,0)
	print "False"

	time.sleep(5)
