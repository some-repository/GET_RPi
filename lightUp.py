def lightUp (ledNumber, period):
    GPIO.output(ledNumber, 1)
    time.sleep (period)
    GPIO.output(ledNumber, 0)

