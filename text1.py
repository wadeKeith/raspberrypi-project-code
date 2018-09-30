#import necessary package
import socket
import time
import os
#import sys
import RPi.GPIO as GPIO
import numpy as np
import cv2
import threading
_lock = threading.Lock()
#define host ip: Rpi's IP
HOST_IP = "192.168.1.104"
HOST_PORT = 8888
print("Starting socket: TCP...")
#1.create socket object:socket=socket.socket(family,type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
#2.bind socket to addr:socket.bind(address)
socket_tcp.bind(host_addr)
#3.listen connection request:socket.listen(backlog)
socket_tcp.listen(1)
#4.waite for client:connection,address=socket.accept()
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
a ="Welcome to RPi TCP server!"
socket_con.send(a.encode())
#5.handle
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT,initial=False)
duo = GPIO.PWM(18,300)
p1 = GPIO.PWM(17,10000)
p2 = GPIO.PWM(27,10000)
en = GPIO.output(22,False)
p1.start(0)
p2.start(0)
duo.start(0)

# start video capture
cap = cv2.VideoCapture(0)

print("Receiving package...")


def forward(a):
    k=a/100
    print("k=%lf"%k)
    p1.ChangeDutyCycle(k)
    p2.ChangeDutyCycle(0)
def back(a):
    k=a/100
    print("k1=%lf"%k)
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(k)
def lr(a):
    duo.ChangeDutyCycle(a) #左满舵a=32，右满舵a=52，中值a=42，则a值取32至52
def stop():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)
    duo.ChangeDutyCycle(42)


def capture():
    # so easy
    _lock.acquire()
    _, frame = cap.read()
    cv2.imwrite('shu.jpg', frame)
    #print('save image ok')
    _lock.release()
    '''
    global x
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('shu.jpg',fourcc,20.0,(width,height))
    ret,frame = cap.read()
    out.write(frame)
    img = cv2.imread('shu.jpg')
    x = open('shu.jpg','rb').read()
    out.release()
    cap.release()
    '''

def sendImage(socket_con):
    _lock.acquire()
    if os.path.isfile('shu.jpg'):
        #send image
        socket_con.sendall(open('shu.jpg', 'rb').read())
        print('send image ok')
    _lock.release()


def run_thread():
    #lock.acquire()
    #try:
        #for i in range(1,50):
    if not cap or not cap.isOpened():
        print('can not open')
        return
    while True:
        capture()
        time.sleep(0.05)# 1s
        #socket_con.sendall(x)
        
    #finally:
     #   lock.release()
def run_thread2():
    #lock.acquire()
    #try:
    while True:
        data=socket_con.recv(1024).decode()
        print("Received:%s"%data)
            #p1.ChangeDutyCycle(int(data))
        ver, value = data.split(':')
        print("this is ver:%s"%ver)
        print("this is value:%d"%int(value))
        if ver == 'L':
            lr(int(value))
        elif ver == 'R':
            lr(int(value))
        elif ver == 'F':
            forward(int(value))
        elif ver == 'B':
            back(int(value))
        # do not use
        #elif ver == 'I':
        #    sendImage(socket_con)
        socket_con.send(data.encode())
        time.sleep(0.05)
    #finally:
        #lock.release()
t1 = threading.Thread(target=run_thread)
#t2 = threading.Thread(target=run_thread2)
t1.start()
#
run_thread2()
#t2.start()
input('cmd:')
t1.join()
t2.join()
socket_tcp.close()
# close cap
if cap and cap.isOpened():
    cap.release()
#sys.exit(1)
GPIO.cleanup()
