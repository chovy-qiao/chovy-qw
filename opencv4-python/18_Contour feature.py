import numpy as np
import cv2 as cv
path = r'D:\PYTHON\timg.jpg'  
im = cv.imread(path)     #读取图像
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)     #二值化
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #寻找图像轮廓
cnt = contours[0]    
M = cv.moments(cnt)
print( M )

# 质心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
# 轮廓面积
area = cv.contourArea(cnt) 
# 轮廓周长
perimeter = cv.arcLength(cnt,True)
#轮廓近似
epsilon = 0.1*cv.arcLength(cnt,True) 
approx = cv.approxPolyDP(cnt,epsilon,True)   #第二个参数为从轮廓到近似轮廓的最大距离】
#凸包曲线
hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]] 
hull = cv.convexHull(cnt) 
#检查凸度
k = cv.isContourConvex(cnt) 
# 边界矩形
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# 旋转矩形
rect = cv.minAreaRect(cnt)  #获得Box2D结构
box = cv.boxPoints(rect)    #获得四个点
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)
# 最小闭合圈
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)
# 椭圆、
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)
# 直线
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
