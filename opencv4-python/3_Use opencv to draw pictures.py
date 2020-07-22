import numpy as np
import cv2 as cv
# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img,(0,0),(511,511),(255,0,0),5)

#绘制矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

#绘制圆圈
cv.circle(img,(447,63), 63, (0,0,255), -1)

#绘制椭圆
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#添加文本
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

#显示图像
cv.imshow('image',img)

