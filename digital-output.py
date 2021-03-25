import RPi.GPIO as GPIO
import time

LEDs = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
for i in LEDs:
    GPIO.setup(i,GPIO.OUT)

bit_depth = 8

def converter (x):
    arr = []
    for i in range (bit_depth - 1, -1, -1):
        if int (x / (2**i)) == 1:
            arr.append (1)
            x = x - 2**i
        else:
            arr.append (0)
        i = i - 1
    return arr

for i in range (bit_depth - 1, -1, -1):
    GPIO.output(LEDs [i], 0)

for j in range (0, 256, 1):
    arr = converter (j)
    print (arr)
    for i in range (bit_depth - 1, -1, -1):
        GPIO.output(LEDs [i], arr [i])
    time.sleep (0.5)
    for i in range (bit_depth - 1, -1, -1):
        GPIO.output(LEDs [i], 0)
