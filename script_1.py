import main_script_module as main

main.GPIOinit ()

def num2dac (value):
	main.lightNumber (value)
inp = 0
while inp != -1:
	print ('Enter value (-1 to exit)')
	inp = int (input ())
	num2dac (inp)

GPIO.cleanup ()