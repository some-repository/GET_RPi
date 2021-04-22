import math
import matplotlib.pyplot as plt
import main_script_module as main
import time
import RPi.GPIO as GPIO

main.GPIOinit ()

def sin_gen (tim, frequency, samplingFrequency):
    omega = 2*(math.pi)*frequency
    n = tim*samplingFrequency
    ndarray = []
    t = []
    for i in range (0, n, 1):
        ndarray.append (int (255 * math.sin(omega*tim*(i/n))))
    for i in range (0, n, 1):
        t.append (i)
    plt.plot (t, ndarray)
    plt.show ()
    t = 1
    while t == 1:
    	try:
    		for i in range (0, n, 1):
        		main.lightNumber (ndarray [i])
        		time.sleep (tim)
    	except: KeyboardInterrupt:
    		t = 0
    		for i in main.LEDs:
        		GPIO.output(i,0)
    		GPIO.cleanup ()

sin_gen (10, 1000, 100)

