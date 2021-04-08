import RPi.GPIO as GPIO
import time

LEDs = [24, 25, 8, 7, 12, 16, 20, 21]
LED_number = 8
bit_depth = 8


GPIO.setmode(GPIO.BCM)
for i in LEDs:
    GPIO.setup(i,GPIO.OUT)
for i in LEDs:
    GPIO.output(i,0)

def lightUp (ledNumber, period):
    ledNumber = LEDs [ledNumber]
    GPIO.output(ledNumber, 1)
    time.sleep (period)
    GPIO.output(ledNumber, 0)

lightUp (5, 1)
GPIO.cleanup()