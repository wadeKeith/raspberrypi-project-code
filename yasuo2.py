from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import cv2
image=cv2.imread("/home/pi/Desktop/shu.jpg")
res = cv2.resize(image, (320,240), interpolation=cv2.INTER_AREA)
cv2.imwrite("/home/pi/Desktop/shu1.jpg",res)
imgE = Image.open("/home/pi/Desktop/shu1.jpg")
gray = imgE.convert("L")
gray.save("/home/pi/Desktop/shu2.jpg")
gary3=gray.point(lambda i:i*0.9)
gary3.save("/home/pi/Desktop/shu5.jpg")