import main_script_module as main
import time

print ('Enter value repetitionsNumber')
repetitionsNumber = int (input ())
main.GPIOinit ()

for i in range (0, repetitionsNumber, 1):

    for j in range (0, 256, 1):
        main.lightNumber (j)
        time.sleep (0.02)
    for j in range (255, -1, -1):
        main.lightNumber (j)
        time.sleep (0.02)