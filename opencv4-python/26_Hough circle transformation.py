import numpy as np
import cv2 as cv
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\time1.png'  
img = cv.imread(path,0)     #读取图像,并转化为灰度图像
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # 绘制外圆
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # 绘制圆心
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()

