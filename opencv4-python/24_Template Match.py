import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\la.png'
img = cv.imread(path,0)
img2 = img.copy()
path1 = r'D:\Laboratory\Study\Computer Vision\opencv4-python\tpl.png'
template = cv.imread(path1,0)
w, h = template.shape[::-1]
# 列表中所有的6种比较方法
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # 应用模板匹配
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)  
    # 如果方法是TM_SQDIFF或TM_SQDIFF_NORMED，则取最小值
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

#%%
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\maliao.png'
img_rgb = cv.imread(path)
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
path1 = r'D:\Laboratory\Study\Computer Vision\opencv4-python\tpl1.png'
template = cv.imread(path1,0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('D:/Laboratory/Study/Computer Vision/opencv4-python/res.png', img_rgb)
