import cv2 as cv
print( cv.__version__ )
import os

#imread函数有两个参数，第一个参数是图片路径，第二个参数表示读取图片的形式
# cv2.IMREAD_COLOR：加载彩色图片，这个是默认参数，可以直接写1
# cv2.IMREAD_GRAYSCALE：以灰度模式加载图片，可以直接写0
# cv2.IMREAD_UNCHANGED：包括alpha，可以直接写-1

path = r"D:\PYTHON\0001TP_006750.png"
a = cv.imread(path,0)
print(a)
# cv.imshow():第一个参数是窗口名称，它是一个字符串。第二个参数是我们的对象
cv.imshow('image',a)
# cv.waitKey() #是一个键盘绑定函数
# cv.destroyAllWindows()#破坏我们创建的所有窗口
# cv.destroyWindow()#在其中传递确切的窗口名称作为参数

cv.imwrite('xxx.jpg',a)

#%% 读取图像并且显示并保存   
import numpy as np
import cv2 as cv
path = r"D:\PYTHON\0001TP_006750.png"
img = cv.imread(path,0)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27:         # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()
    

#%%    
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r"D:\PYTHON\0001TP_006750.png"
img = cv.imread(path,0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
plt.show()