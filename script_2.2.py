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
    i = 0
    for i in main.LEDs:
        GPIO.output(i,0)
    i = 0
    time.sleep (0.1)
    inp = GPIO.input (4)
    while (inp == 1) & (i < 255):
        i = i + 1
        num2dac (i)
        time.sleep (0.002)
        inp = GPIO.input (4)
    print ('Digital value: ', i, 'Analog value: ', i*(3.3/255), ' V')
    time.sleep (0.4)

GPIO.cleanup ()