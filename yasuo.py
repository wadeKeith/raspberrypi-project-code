import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

###################导入计算机视觉库opencv和图像处理库PIL####################
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import cv2
import time
time1 = time.time()
####################读入图像###############################
image=cv2.imread("/home/pi/Desktop/shu.jpg")

####################双三次插值#############################
res = cv2.resize(image, (640,480), interpolation=cv2.INTER_AREA)

####################写入图像########################
cv2.imwrite("/home/pi/Desktop/shu1.jpg",res)

###########################图像对比度增强##################
imgE = Image.open("/home/pi/Desktop/shu1.jpg")
#imgEH = ImageEnhance.Contrast(imgE)
#img1=imgEH.enhance(2.8)

########################图像转换为灰度图###############
gray = imgE.convert("L")
gray.save("/home/pi/Desktop/shu2.jpg")

##########################图像增强###########################

# 创建滤波器，使用不同的卷积核
#gary2=gray.filter(ImageFilter.DETAIL)
#gary2.save("/home/pi/Desktop/shu3.jpg")

#############################图像点运算#################
gary3=gray.point(lambda i:i*0.9)
gary3.save("/home/pi/Desktop/shu5.jpg")
# img1.show("new_picture")
time2=time.time()
print (u'总共耗时：' + str(time2 - time1) + 's')