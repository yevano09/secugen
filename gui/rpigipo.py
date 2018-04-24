import RPi.GPIO as GPIO
#for the sleep method
import time


led = 8
#set numbering mode for the program
GPIO.setmode(GPIO.BOARD)
#setup led(pin 8) as output pin
GPIO.setup(led, GPIO.OUT,initial=0)

def ledGlow(numberofTimes=0):
	try:
		#turn on and off the led in intervals of 1 second
		for x in range(0, numberofTimes):
			#turn on, set as HIGH or 1
			GPIO.output(led,GPIO.HIGH)
			print("ON")
			time.sleep(1)
			#turn off, set as LOW or 0
			GPIO.output(led, GPIO.LOW)
			print("OFF")
			time.sleep(1)
	except KeyboardInterrupt:
		#cleanup GPIO settings before exiting
		print("KeyboardInterrupt occured")
	finally:
		GPIO.cleanup()
		print("Exiting..")



if  __name__ == '__main__':
	ledGlow(5)

