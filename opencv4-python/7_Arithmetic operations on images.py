import numpy as np
import cv2 as cv
x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255
print( x+y )          # 250+10 = 260 % 256 = 4
# OpenCV加法和Numpy加法之间有区别。OpenCV加法是饱和运算，而Numpy加法是模运算
#%%   图像融合
import numpy as np
import cv2 as cv
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\333.jpg'
path1 = r'D:\Laboratory\Study\Computer Vision\opencv4-python\22.jpg'
img1 = cv.imread(path)
img2 = cv.imread(path1)
# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#%% 换位运算
# 加载两张图片
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')
# 我想把logo放在左上角，所以我创建了ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# 现在创建logo的掩码，并同时创建其相反掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)       #灰度化
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)    #二值化
mask_inv = cv.bitwise_not(mask)     #mask掩膜
# 现在将ROI中logo的区域涂黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# 仅从logo图像中提取logo区域
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# 将logo放入ROI并修改主图像
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()