import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\fenshuiling.png'  
#读取图像,并转化为灰度图像,进行阈值分割
#可以在前面加上一个去噪的步骤
# blurred = cv.pyrMeanShiftFiltering(src, sp, sr)
img = cv.imread(path)     
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
# cv.imshow('x',thresh)

# 噪声去除(开环)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
SURE_BG = cv.dilate(opening,kernel,iterations = 3)
# cv.imshow('x',SURE_BG)

# 寻找距离
# 寻找前景区域
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
# dist_output = cv.normalize(dist_transform,0,1.0,cv.NORM_MINMAX)
# cv.imshow('xx',dist_output)

ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# cv.imshow('xxx',sure_fg)
# 找到未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(SURE_BG,sure_fg)
# 类别标记
ret, markers = cv.connectedComponents(sure_fg)
# 为所有的标记加1，保证背景是0而不是1
markers = markers+1
# 现在让所有的未知区域为0
markers[unknown==255] = 0

markers = cv.watershed(img,markers) 
img[markers == -1] = [255,0,0]
cv.imshow('results',img)