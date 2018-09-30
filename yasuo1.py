import cv2
#img = cv2.imread("/home/pi/Desktop/shu.jpg", cv2.IMREAD_GRAYSCALE)
#cv2.imwrite('/home/pi/Desktop/shu1.jpg', img)
img1 = cv2.imread("/home/pi/Desktop/shu.jpg")
res = cv2.resize(img1, (640,480), interpolation=cv2.INTER_AREA)
Grayimg = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(Grayimg, 12, 255,cv2.THRESH_BINARY)
cv2.imwrite('/home/pi/Desktop/shu2.jpg', thresh)