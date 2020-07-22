import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)   #参数为设备索引或者视频文件
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示结果帧e
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv.destroyAllWindows()

#cap.get(propId)方法访问该视频的某些功能其中propId是0到18之间的一个数字。
#每个数字表示视频的属性（如果适用于该视频），并且可以显示完整的详细信息在这里看到：
# 例如，我可以通过cap.get(cv.CAP_PROP_FRAME_WIDTH)和cap.get(cv.CAP_PROP_FRAME_HEIGHT)检查框架的宽度和高度。
# 默认情况下，它的分辨率为640x480。但我想将其修改为320x240。只需使用和即可。
# ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240).

#%%
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

#%%
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# 定义编解码器并创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'XVID')   
out = cv.VideoWriter('D:\实验室\学习\计算机视觉\opencv4-python\output.avi', fourcc, 20.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)  
    # 写翻转的框架
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# 完成工作后释放所有内容
cap.release()
out.release()
cv.destroyAllWindows()