# Shi-tomas拐角检测器
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'  
img = cv.imread(path)     #读取图像
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)
plt.imshow(img)

