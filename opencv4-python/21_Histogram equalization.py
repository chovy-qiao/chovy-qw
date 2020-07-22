# 计算步骤：
# 1.计算累计直方图（累计概率相加）
# 2.将累计直方图进行区间转换(最大灰度及乘累计概率)
# 3.在累计直方图中，概率相近的原始值会被处理为相同的值（得到均衡化的直方图）
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\junhenghua.png'  
img = cv.imread(path,0)     #读取图像,并转化为灰度图像
equ = cv.equalizeHist(img)      #输入为灰度图，输出为处理后的均衡图像
res = np.hstack((img,equ)) #j合并图像
cv.imshow('tu',res)
plt.hist(img.ravel(),256)
plt.figure()
plt.hist(equ.ravel(),256)
#%%
# subplot(nrows,ncols,plot_number)
# 参数:行数，列数，窗口序号
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\zishiyingjunhenghua.png'  
img = cv.imread(path,0)     #读取图像,并转化为灰度图像
equ = cv.equalizeHist(img)      #输入为灰度图，输出为处理后的均衡图像
#clipLimit颜色对比度的阈值， titleGridSize进行像素均衡化的网格大小
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))   
cl1 = clahe.apply(img)
plt.subplot(2,2,1),plt.imshow(img,'gray'),plt.title('ORIGINAL'),plt.axis('off')
plt.subplot(2,2,2),plt.imshow(equ,'gray'),plt.title('jieguo'),plt.axis('off')
plt.subplot(2,2,3),plt.imshow(cl1,'gray'),plt.title('jieguo1'),plt.axis('off')