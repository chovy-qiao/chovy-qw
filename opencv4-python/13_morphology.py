#腐蚀运算
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%  膨胀运算
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.dilate(img,kernel,iterations = 1) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%   开运算
import random
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
#给图像加噪声
def GaessNoisy(src, sigma):
    NoiseImg = src.copy()
    s = np.random.normal(0, 1, size=src.shape)*sigma
    NoiseImg = np.add(NoiseImg, s)
    NoiseImg.astype(dtype=np.uint8)
    return NoiseImg
img = GaessNoisy(img, 20)
kernel = np.ones((5,5),np.uint8)
erosion = cv.morphologyEx(img, cv.MORPH_OPEN, kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%   开运算
import random
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
#给图像加噪声
def GaessNoisy(src, sigma):
    NoiseImg = src.copy()
    s = np.random.normal(0, 1, size=src.shape)*sigma
    NoiseImg = np.add(NoiseImg, s)
    NoiseImg.astype(dtype=np.uint8)
    return NoiseImg
img = GaessNoisy(img, 20)
kernel = np.ones((5,5),np.uint8)
erosion = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
#%%   形态学梯度
import random
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
#给图像加噪声
def GaessNoisy(src, sigma):
    NoiseImg = src.copy()
    s = np.random.normal(0, 1, size=src.shape)*sigma
    NoiseImg = np.add(NoiseImg, s)
    NoiseImg.astype(dtype=np.uint8)
    return NoiseImg
img = GaessNoisy(img, 20)
kernel = np.ones((5,5),np.uint8)
erosion = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
#%% 顶帽
import random
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
#给图像加噪声
def GaessNoisy(src, sigma):
    NoiseImg = src.copy()
    s = np.random.normal(0, 1, size=src.shape)*sigma
    NoiseImg = np.add(NoiseImg, s)
    NoiseImg.astype(dtype=np.uint8)
    return NoiseImg
img = GaessNoisy(img, 20)
kernel = np.ones((5,5),np.uint8)
erosion = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%% 帽
import random
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
#给图像加噪声
def GaessNoisy(src, sigma):
    NoiseImg = src.copy()
    s = np.random.normal(0, 1, size=src.shape)*sigma
    NoiseImg = np.add(NoiseImg, s)
    NoiseImg.astype(dtype=np.uint8)
    return NoiseImg
img = GaessNoisy(img, 20)
kernel = np.ones((5,5),np.uint8)
erosion = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel) 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
#%%结构元素
# 矩形内核
cv.getStructuringElement(cv.MORPH_RECT,(5,5))
# 椭圆内核
cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
#十字内核
cv.getStructuringElement(cv.MORPH_CROSS,(5,5))