import numpy as np
import cv2 as cv
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\chengshi.jpg'
img = cv.imread(path)
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('D:/Laboratory/Study/Computer Vision/opencv4-python/sift_keypoints.jpg', img)

img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
cv.imwrite('sift_keypoints.jpg',img)

sift = cv.xfeatures2d.SIFT_create() 
kp, des = sift.detectAndCompute(gray,None)
