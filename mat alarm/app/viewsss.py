
import RPi.GPIO as GPIO
from gpiozero import Buzzer
GPIO.setmode(GPIO.BOARD)
but4=1
led1=10
GPIO.setwarnings(False)
while True:
	GPIO.setup(10,GPIO.OUT)
	GPIO.output(10,GPIO.LOW)
GPIO.cleanup()
