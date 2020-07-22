import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\timg.jpg'  
img = cv.imread(path,0)     #读取图像,并转化为灰度图像
#hist函数：第一个参数：图像；第二个参数：像素级
#img.Ravel()：将多维数组转化为一维数组
plt.hist(img.ravel(),256,[0,256]); plt.show()


#%%
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\timg.jpg'  
img = cv.imread(path)     #读取图像,并转化为灰度图像
# 查找直方图
# images：它是uint8或float32类型的源图像。它应该放在方括号中，即“ [img]”。
# channels：也以方括号给出。它是我们计算直方图的通道的索引。例如，如果输入为灰度图像，则其值为[0]。对于彩色图像，您可以传递[0]，[1]或[2]分别计算蓝色，绿色或红色通道的直方图。
# mask：图像掩码。为了找到完整图像的直方图，将其指定为“无”。但是，如果要查找图像特定区域的直方图，则必须为此创建一个掩码图像并将其作为掩码。（我将在后面显示一个示例。）
# histSize：这表示我们的BIN计数。需要放在方括号中。对于全尺寸，我们通过[256]。
# ranges：这是我们的RANGE。通常为[0,256]。
hist = cv.calcHist([img],[0],None,[256],[0,256])
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])    #指定线条颜色
    plt.show()
    
#numpy寻找直方图
hist,bins = np.histogram(img.ravel(),256,[0,256])
hist = np.bincount(img.ravel()，minlength = 256)

#%%掩膜
# mask = np.zeros(images,shape,np.uint8)
# mask[200:400;200:400]    掩膜图像白底
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\timg.jpg'  
img = cv.imread(path,0)     #读取图像,并转化为灰度图像
mask = np.zeros(img.shape,np.uint8)
mask[200:400,200:400] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)
# cv.imshow('2',masked_img)
hist = cv.calcHist([img],[0],mask,[256],[0,256])
hist1 = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist1)
plt.plot(hist)
