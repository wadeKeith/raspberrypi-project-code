import cv2
import numpy as np
def a():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('shu.jpg',fourcc,20.0,(width,height))
    while(cap.isOpened()):
    #for i in range(1,100):
        ret,frame = cap.read()
        if ret == True:
            out.write(frame)
        #a=input('cmd:')
        #if a =='q':
            img = cv2.imread('shu.jpg')
            x = img.tobytes()
            return x
            break
    
        
    #    cv2.imshow('My Camera',frame)
     #   if(cv2.waitKey(0) & 0xFF) == ord('q'):
      #      break
       # else:
        #    break
    out.release()
    cap.release()
