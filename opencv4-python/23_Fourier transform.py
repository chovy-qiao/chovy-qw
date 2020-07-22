import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\juzi.png'  
img = cv.imread(path) 

# numpy实现傅里叶变换
f = np.fft.fft2(img)       #实现傅里叶变化，返回复数数组
fshift = np.fft.fftshift(f)    #将零频率分量移动到频谱中心
magnitude_spectrum = 20*np.log(np.abs(fshift))    #设置频谱范围
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#%% numpy实现傅里叶变换,高通滤波器
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'  
img = cv.imread(path,0)
#提取频谱图
f = np.fft.fft2(img)      
fshift = np.fft.fftshift(f)
#高通滤波器       
rows, cols = img.shape
crow,ccol = int(rows/2),int(cols/2)
fshift[crow-30:crow+31, ccol-30:ccol+31] = 0    #将频谱图的中心涂黑
ishift = np.fft.ifftshift(fshift)  #将零频率移动回左上角（逆变换）
iimg = np.fft.ifft2(ishift)       
iimg = np.abs(iimg)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(iimg, cmap = 'gray')
plt.title('xx'), plt.xticks([]), plt.yticks([])
plt.show()

#%%   numpy实现逆傅里叶变换
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'  
img = cv.imread(path)
# numpy实现傅里叶变换
f = np.fft.fft2(img)       #实现傅里叶变化，返回复数数组
fshift = np.fft.fftshift(f)    #将零频率分量移动到频谱中心
ishift = np.fft.ifftshift(fshift)  #将零频率移动回左上角（逆变换）
iimg = np.fft.ifft2(ishift)        #逆傅里叶变换
iimg = np.abs(iimg)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(iimg, cmap = 'gray')
plt.title('xx'), plt.xticks([]), plt.yticks([])
plt.show()

#%% opencv实现傅里叶变换
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'  
img = cv.imread(path,0)
#opencv中原始图像需要转换成float格式；cv.DFT_COMPLEX_OUTPUT：指定输出类型
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)   #得到频谱值，双通道：实数；虚数
dft_shift = np.fft.fftshift(dft)       #低频移到中心
# cv.magnitude：将双通道的数据集转换到0-255
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))  
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

#%% opencv实现逆傅里叶变换
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\qingshi.png'  
img = cv.imread(path,0)
#正傅里叶变换
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)   
fshift = np.fft.fftshift(dft)
#逆傅里叶变换
ishift = np.fft.ifftshift(fshift)
iimg = cv.idft(ishift)
iimg = cv.magnitude(iimg[:,:,0],iimg[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(iimg, cmap = 'gray')
plt.title('xx'), plt.xticks([]), plt.yticks([])
plt.show() 

#%%低通滤波器
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\333.jpg'  
img = cv.imread(path,0)
#提取频谱图
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)   
fshift = np.fft.fftshift(dft)
#低通滤波器       
rows, cols = img.shape
crow,ccol = int(rows/2),int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+31, ccol-30:ccol+31] = 1    #将频谱图的中心涂白
ishift = fshift*mask
ishift = np.fft.ifftshift(fshift)  #将零频率移动回左上角（逆变换）
iimg = cv.idft(ishift)
iimg = cv.magnitude(iimg[:,:,0],iimg[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(iimg, cmap = 'gray')
plt.title('xx'), plt.xticks([]), plt.yticks([])
plt.show()

   


