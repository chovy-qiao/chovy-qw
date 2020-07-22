import cv2 as cv
import numpy as np
path = path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\chedao.png'
img = cv.imread(cv.samples.findFile(path))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)      #灰度化
edges = cv.Canny(gray,50,150,apertureSize = 3)  #canny边缘检测
lines = cv.HoughLines(edges,1,np.pi/180,200)   #图片，步长，角度，阈值分割的低值
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow('img',img)
# cv.imwrite('D:/Laboratory/Study/Computer Vision/opencv4-python/r.png', img_rgb)

#%%概率霍夫变换
import cv2 as cv
import numpy as np
path = path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\chedao.png'
img = cv.imread(cv.samples.findFile(path))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)      #灰度化
edges = cv.Canny(gray,50,150,apertureSize = 3)  #canny边缘检测
#maxLineGap：断点像个像素
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)       
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv.imshow('img',img)
# cv.imwrite('houghlines5.jpg',img)
