import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\timg.jpg'  
img = cv.imread(path)  
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([img], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist,interpolation = 'nearest')
plt.show()
