import RPi.GPIO as GPIO
import time

LEDs = [10, 9, 11, 5, 6, 13, 19, 26]
LED_number = 8
bit_depth = 8

def GPIOinit ():
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
    #time.sleep (1)

def runningPattern(pattern, direction):
    pattern_copy = pattern
    if direction == 1:
        while int ((pattern / 256)) == 0:
            pattern = pattern << 1
        while (pattern % 2) == 0:
            pattern = pattern >> 1
            lightNumber (pattern)
            time.sleep (1)
    elif direction == 0:
        while int ((pattern / 256)) == 0:
            lightNumber (pattern)
            pattern = pattern << 1
            time.sleep (1)
    runningPattern (pattern_copy, direction)

	


GPIOinit ()
#lightUp (1, 1)
#blink (0, 10, 0.5)
#runningLight (3, 0.5)
#runningDark (4, 0.5)
#lightNumber (123)
#time.sleep (1)
#runningPattern (5, 1)
#runningPattern (7, 0)

GPIO.cleanup ()

