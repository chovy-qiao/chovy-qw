path = r'D:\Laboratory\Study\Computer Vision\opencv4-python\chengshi.jpg'
img = cv.imread(path)
# 创建SURF对象。你可以在此处或以后指定参数。
# 这里设置海森矩阵的阈值为400
surf = cv.xfeatures2d.SURF_create(400)
# 直接查找关键点和描述符
kp, des = surf.detectAndCompute(img,None)



# 检查海森矩阵阈值
print( surf.getHessianThreshold() )

# 我们将其设置为50000。记住，它仅用于表示图片。 
# 在实际情况下，最好将值设为300-500
surf.setHessianThreshold(50000)
# 再次计算关键点并检查其数量。
>>> kp, des = surf.detectAndCompute(img,None)
print( len(kp) )

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()


# 检查flag标志，如果为False，则将其设置为True
print( surf.getUpright() )

surf.setUpright(True)
# 重新计算特征点并绘制
kp = surf.detect(img,None)
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()


# 找到算符的描述
print( surf.descriptorSize() )

# 表示flag “extened” 为False。
surf.getExtended()

# 因此，将其设为True即可获取128个尺寸的描述符。
surf.setExtended(True)
print( des.shape )

