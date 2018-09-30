
import time
import numpy as np
import cv2
import threading
lock = threading.Lock()
def p():
    global x
    cap = cv2.VideoCapture(0)
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
def run_thread():
    lock.acquire()
    try:
        p()
    finally:
        lock.release()

t1 = threading.Thread(target=run_thread)
t1.start()
t1.join()
#open('abc.text','w').write(x.decode())
#print(x[:100])
#open('abc.jpg','wb').write(x)
    
