import numpy as np
import cv2 as cv
path = r'D:\PYTHON\timg.jpg'  
im = cv.imread(path)     #读取图像
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)     #二值化
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #寻找图像轮廓
cnt = contours[0]  
#边界框长宽比
x,y,w,h = cv.boundingRect(cnt)    #得到边界框尺寸
aspect_ratio = float(w)/h

#范围：轮廓区域面积和边界框面积之比
area = cv.contourArea(cnt)    #轮廓区域的面积
x,y,w,h = cv.boundingRect(cnt)    
rect_area = w*h              #边界框面积
extent = float(area)/rect_area     
print(extent)

#坚实度：等高线面积与凸包面积之比
area = cv.contourArea(cnt)     #等高线面积
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)     #凸包面积
solidity = float(area)/hull_area

#等效直径：等效直径是面积与轮廓面积相同的圆的直径。
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

#取向：指物体指向的角度
(x,y),(MA,ma),angle = cv.fitEllipse(cnt)

#掩码和像素点,将图像的感兴趣区域提取出来
mask = np.zeros(imgray.shape,np.uint8)   
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)

#最大值，最小值和他们的位置
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)

#平均颜色或者平均强度
mean_val = cv.mean(im,mask = mask)

#极端点 ：极点是指对象的最顶部，最底部，最右侧和最左侧的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])    
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])   
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])   
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])  

