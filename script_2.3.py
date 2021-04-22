import main_script_module as main
import RPi.GPIO as GPIO
import time

GPIO.cleanup ()
main.GPIOinit ()
GPIO.setup (17, GPIO.OUT)
GPIO.setup (4, GPIO.IN)
GPIO.output (17, 1)

def num2dac (value):
	main.lightNumber (value)

while 1:
    value = 0
    for i in range (7, -1, -1):
        value = value + 2**i
        #print (value)
        num2dac (value)
        time.sleep (0.005)
        inp = GPIO.input (4)
        if inp == 0:
            value = value - 2**i
    print ('Digital value: ', value, 'Analog value: ', value*(3.3/255), ' V')
    time.sleep (0.4)

GPIO.cleanup ()