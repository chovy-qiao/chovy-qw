#图像过滤
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'
img = cv.imread(path)
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

#%%   平均模糊
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'
img = cv.imread(path)
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%    高斯模糊
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'
img = cv.imread(path)
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'
img = cv.imread(path)
blur = cv.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%   中位模糊
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\PYTHON\timg.jpg'
img = cv.imread(path)
blur = cv.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#%%   双边模糊
blur = cv.bilateralFilter(img,9,75,75)
