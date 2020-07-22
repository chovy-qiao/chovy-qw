import numpy as np
import cv2 as cv

# e1 = cv.getTickCount()
# # 你的执行代码
# e2 = cv.getTickCount()
# time = (e2 - e1)/ cv.getTickFrequency()

path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\333.jpg'
img1 = cv.imread(path)
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)      #中值滤波
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print(t)

#%%   检查是否用了优化，启动和禁用优化
cv.useOptimized()

timeit res = cv.medianBlur(img,49)

#关闭它
cv.setUseOptimized(False)
cv.useOptimized()

timeit res = cv.medianBlur(img,49)

