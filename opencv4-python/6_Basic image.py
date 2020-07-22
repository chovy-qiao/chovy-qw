import numpy as np
import cv2 as cv
path = r'D:\PYTHON\timg.jpg'  #不能有中文路径
img = cv.imread(path)     #读取图像

#返回三通道的数组
px = img[100,100]
print(px)

#单通道
a = img[100,100,1]
print(a)

# 修改像素值
img[100,100] = [255,255,255]
print( img[100,100] )

#用numpy的方式修改像素值 
img.item(10,10,2)
img.itemset((10,10,2),100)
c = img.item(10,10,2)
print(c)

#%%
#访问图像属性
print(img.shape)      #行列通道数
print(img.size)       #像素总数
print(img.dtype)      #数据类型

#ROI
cc = img[280:340, 330:390]
img[273:333, 100:160] = cc 
# cv.imshow('img',img)

#拆分和合并图像通道
b,g,r = cv.split(img)
# cv.imshow('b',b)
img = cv.merge((b,g,r))
#使用numpy索引
b = img [:, :, 0]
#让所有0通道的像素值都为0
img [:, :, 0] = 0

#%%
# src - 输入图像
# top，bottom，left，right 边界宽度（以相应方向上的像素数为单位）
# borderType - 定义要添加哪种边框的标志。它可以是以下类型：
# cv.BORDER_CONSTANT - 添加恒定的彩色边框。该值应作为下一个参数给出。
# cv.BORDER_REFLECT - 边框将是边框元素的镜像，如下所示： fedcba | abcdefgh | hgfedcb
# **cv.BORDER_REFLECT_101**或 **cv.BORDER_DEFAULT**与上述相同，但略有变化，例如： gfedcb | abcdefgh | gfedcba
# **cv.BORDER_REPLICATE**最后一个元素被复制，像这样： aaaaaa | abcdefgh | hhhhhhh
# **cv.BORDER_WRAP**难以解释，它看起来像这样： cdefgh | abcdefgh | abcdefg
# value -边框的颜色，如果边框类型为**cv.BORDER_CONSTANT**
# 下面是一个示例代码，演示了所有这些边框类型，以便更好地理解：
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()