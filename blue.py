import serial
import sys
port = "/dev/rfcomm0"
serial = serial.Serial(port,115200)
sendstr1="F"
sendstr2=25
serial.write(encode(sendstr1))
serial.write(sendstr2)
serial.flushInput()
    