import main_script_module as main
import RPi.GPIO as GPIO

def num2dac (value):
	main.lightNumber (value)
main.GPIOinit ()
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,1)

inp = 0
while inp != -1:
	print ('Enter value (-1 to exit)')
	inp = int (input ())
	#print ('Enter value (-1 to exit)')
	print (inp, ' = ', (inp/255)*3.3, 'V')
	num2dac (inp)

GPIO.cleanup ()
