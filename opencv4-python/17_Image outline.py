import numpy as np
import cv2 as cv
path = r'D:\PYTHON\timg.jpg'  #不能有中文路径
im = cv.imread(path)     #读取图像
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# indcontour()函数中有三个参数，第一个是源图像，第二个是轮廓检索模式，第三个是轮廓逼近方法。
# 输出等高线和层次结构。轮廓是图像中所有轮廓的Python列表。每个单独的轮廓是一个(x,y)坐标的Numpy数组的边界点的对象。
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im, contours, -1, (0,255,0), 3)
cv.imshow('xx',im)
# # cv.drawContours:第一个参数：原始图像， 2.边缘数组， 3.边缘索引，如果全部绘制则为-1 4.绘制的颜色 5.绘制的轮廓，即画笔粗细
# cnt = contours[4]
# cv.drawContours(img, [cnt], 0, (0,255,0), 3)
