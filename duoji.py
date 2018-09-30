import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(18,RPi.GPIO.OUT,initial=False)
p = RPi.GPIO.PWM(18,300)
p.start(0)
def one():#45 degree servo
    p.ChangeDutyCycle(32)
def two():#90 degree servo
    p.ChangeDutyCycle(42)
def three():#135 degree servo
    p.ChangeDutyCycle(52)
while(True):
    cmd = input('cmd:')
    if cmd =='a':
        one()
    elif cmd =='b':
        two()
    elif cmd =='c':
        three()
    elif cmd =='quit':
        print("out")
        break
RPi.GPIO.cleanup()
