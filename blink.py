def blink (ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount, 1):
        lightUp (ledNumber, blinkPeriod)
        time.sleep (period)