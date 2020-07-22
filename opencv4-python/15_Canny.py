#Canny 边缘检测
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'
img = cv.imread(path,0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

