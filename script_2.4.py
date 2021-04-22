import main_script_module as main
import RPi.GPIO as GPIO
import time
import main_script as main_LED

LEDs_1 = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.cleanup ()
main.GPIOinit ()
main_LED.GPIOinit ()
GPIO.setup (17, GPIO.OUT)
GPIO.setup (4, GPIO.IN)
GPIO.output (17, 1)

def num2dac (value):
	main.lightNumber (value)

while 1:
    value = 0
    #for i in main_LED.LEDs:
     #   GPIO.output(i,0)
    for i in range (7, -1, -1):
        value = value + 2**i
        #print (value)
        num2dac (value)
        time.sleep (0.001)
        inp = GPIO.input (4)
        if inp == 0:
            value = value - 2**i
    #print ('Digital value: ', value, 'Analog value: ', value*(3.3/255), ' V')
    vb = round (value / 32)
    for i in range (0, vb, 1):
        GPIO.output (main_LED.LEDs [i], 1)
    for i in range (vb, 8, 1):
        GPIO.output (main_LED.LEDs [i], 0)
    #time.sleep (0.01)

GPIO.cleanup ()