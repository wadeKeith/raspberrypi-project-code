import cv2
cap = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
while(cap.isOpened()):
    success, frame = cap.read()
    if success==True:
        frame = cv2.flip(frame,0)
        videoWriter.write(frame)
        #cv2.imshow('frame',frame)
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
