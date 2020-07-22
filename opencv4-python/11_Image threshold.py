import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#简单阈值
path = r'D:\PYTHON\timg.jpg'  
img = cv.imread(path)     #读取图像
#第一个参数是图像，第二个是阈值，第三个是像素最大值，第四个是不同类型的阈值
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#%%自适应阈值
path = r'D:\PYTHON\timg.jpg'  
img = cv.imread(path)     #读取图像
img1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# dst = cv2.adaptiveThreshold(src, maxval, thresh_type, type, Block Size, C)
# 输入参数：
# 1. src： 输入图，只能输入单通道图像，通常来说为灰度图
# 2. maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
# 3. thresh_type： 阈值的计算方法，包含以下2种类型：
# cv2.ADAPTIVE_THRESH_MEAN_C：            区域内均值
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C：    区域内像素点加权和，权重为一个高斯窗口
# 4. type：二值化操作的类型，与固定阈值函数相同，用于控制参数2 maxval，包含以下5种类型：
# cv2.THRESH_BINARY： 黑白二值
# cv2.THRESH_BINARY_INV：黑白二值反转
# cv2.THRESH_TRUNC：
# cv2.THRESH_TOZERO：
# cv2.THRESH_TOZERO_INV：
# 5. Block Size： 图片中区域的大小
# 6. C ：阈值计算方法中的常数项

thresh1 = cv.adaptiveThreshold(img1, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
cv.imshow('ss',thresh1)

#%%   ostu二值化
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'  
img = cv.imread(path)     #读取图像
# 全局阈值
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu阈值
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY,cv.THRESH_OTSU)
# 高斯滤波后再采用Otsu阈值
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY,cv.THRESH_OTSU)
# 绘制所有图像及其直方图
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

