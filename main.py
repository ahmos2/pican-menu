BCM_S1_SW_PIN=24
BCM_S2_SW_PIN=23

import RPi.GPIO as GPIO
from subprocess import call
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(BCM_S1_SW_PIN, GPIO.IN)
GPIO.setup(BCM_S2_SW_PIN, GPIO.IN)

menuposition=0
awaitNullInput=1

while True:
	S1_SW=GPIO.input(BCM_S1_SW_PIN)
	S2_SW=GPIO.input(BCM_S2_SW_PIN)
	
	if awaitNullInput==1:
		if S1_SW==1 and S2_SW==1:
			awaitNullInput=0
	else:
		if S1_SW==0:
			call(["espeak",str(menuposition)])
		elif S2_SW==0:
			menuposition+=1
			print(menuposition)
	time.sleep(0.2)
