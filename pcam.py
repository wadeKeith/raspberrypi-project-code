import picamera
import picamera.array
import time
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 30
    print("start preview direct from GPU")
    camera.start_preview()
    time.sleep(10)
    print("end preview")