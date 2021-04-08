import math
import matplotlib.pyplot as plt
import main_script_module as main
import time

main.GPIOinit ()

def sin_gen (time, frequency, samplingFrequency):
    omega = 2*(math.pi)*frequency
    n = time*samplingFrequency
    ndarray = []
    t = []
    for i in range (0, n, 1):
        ndarray.append (int (255 * math.sin(omega*time*(i/n))))
    for i in range (0, n, 1):
        t.append (i)
    plt.plot (t, ndarray)
    plt.show ()
    for i in range (0, n, 1):
        main.lightNumber (ndarray [i])
        time.sleep (0.01)

sin_gen (1, 10, 100)

