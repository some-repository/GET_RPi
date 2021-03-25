import RPi.GPIO as GPIO
import time

LEDs = [24, 25, 8, 7, 12, 16, 20, 21]
LED_number = 8
bit_depth = 8

GPIO.setmode(GPIO.BCM)
for i in LEDs:
    GPIO.setup(i,GPIO.OUT)

def lightUp (ledNumber, period):
    ledNumber = LEDs [ledNumber]
    GPIO.output(ledNumber, 1)
    time.sleep (period)
    GPIO.output(ledNumber, 0)

def lightDown (ledNumber, period):
    ledNumber = LEDs [ledNumber]
    GPIO.output(ledNumber, 0)
    time.sleep (period)
    GPIO.output(ledNumber, 1)

def blink (ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount, 1):
        lightUp (ledNumber, blinkPeriod)
        time.sleep (blinkPeriod)

def runningLight (count, period):
    for i in range (0, count, 1):
        for i in range (0, LED_number, 1):
            lightUp (i, period)

def runningDark (count, period):
    for i in range (0, count, 1):
        for i in LEDs:
            GPIO.output(i, 1)
        for i in range (0, LED_number, 1):
            lightDown (i, period)
    for i in LEDs:
            GPIO.output(i, 0)

def decToBinList (decNumber):
    arr = []
    for i in range (bit_depth - 1, -1, -1):
        if int (decNumber / (2**i)) == 1:
            arr.append (1)
            decNumber = decNumber - 2**i
        else:
            arr.append (0)
        i = i - 1
    return arr

def lightNumber (number):
    arr = decToBinList (number)
    for i in range (0, bit_depth, 1):
        GPIO.output(LEDs [7 - i], arr [i])
    time.sleep (10)


#lightUp (1, 1)
#blink (0, 10, 0.5)
#runningLight (3, 0.5)
#runningDark (4, 0.5)
lightNumber (123)

GPIO.cleanup ()

