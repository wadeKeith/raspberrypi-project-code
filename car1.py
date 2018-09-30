import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(17,RPi.GPIO.OUT)
RPi.GPIO.setup(27,RPi.GPIO.OUT)
p1 = RPi.GPIO.PWM(17,10000)
p2 = RPi.GPIO.PWM(27,10000)
p1.start(0.1)
p2.start(0)
input('cmd:')
p1.stop()
p2.stop()
RPi.GPIO.cleanup()


