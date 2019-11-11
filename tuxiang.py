import numpy as np
import sys
import cv2
import os
from scipy import ndimage

# 创建一个黑色正方体图形
# img = np.zeros((3,3),dtype = np.uint8)
# print(img)
# img= cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# print(img)


# image = cv2.imread("C://Users//zy//Desktop//notepad++//test.png")
# cv2.imwrite('C://Users//zy//Desktop//notepad++//test.jpg',image)
# grayImage = cv2.imread('C://Users//zy//Desktop//notepad++//test1.png',cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('C://Users//zy//Desktop//notepad++//tesrrt.png',grayImage)
# cv2.namedWindow("Image")
# cv2.imshow("Image", grayImage)
# cv2.waitKey(0)
# byteArray = bytearray(image)
# print(byteArray[2])
# randomByteArray= bytearray(os.urandom(120000))
# flatNumpyArray = np.array(randomByteArray)
# grayImage=flatNumpyArray.reshape(300,400)
# cv2.imwrite('C://Users//zy//Desktop//notepad++//RandomGray.png',grayImage)
# bgrImage = flatNumpyArray.reshape(100,400,3)
# cv2.imwrite('C://Users//zy//Desktop//notepad++//RandomColor.png',bgrImage)


# grayImage=cv2.imread('C://Users//zy//Desktop//notepad++//RandomGray.png')
# grayImage[0,0] = [255,255,255]
# cv2.namedWindow("Image")
# cv2.imshow("Image",grayImage)
# cv2.waitKey(0)


# img =cv2.imread('C://Users//zy//Desktop//notepad++//zy.jpg')
# print(img.item(150,120,2))
# img.itemset((150,120,2),255)
# print(img.item(150,120,2))


# img =cv2.imread('C://Users//zy//Desktop//notepad++//zy.jpg')
# print(img.item(150,120,2))
# img[:,:, 1] = 0
# print(img.item(150,120,2))
# print(img.item(150,120,1))
# print(img.item(150,120,0))
# cv2.namedWindow("Image")
# cv2.imshow("Image",img)
# cv2.waitKey(0)




# img =cv2.imread('C://Users//zy//Desktop//notepad++//zy.jpg')
# print(img.size)
# my_roi=img[0:400,0:400]
# img[400:800,400:800]=my_roi
# cv2.namedWindow("Image")
# cv2.imshow("Image",img)
# cv2.waitKey(0)

# videoCapture=cv2.VideoCapture('C://Users//zy//Desktop//notepad++//zy1.avi')
# fps = videoCapture.get(cv2.CAP_PROP_FPS)
# size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        # int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videoWrite = cv2.VideoWriter('C://Users//zy//Desktop//notepad++//zy2.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

# success, frame = videoCapture.read()
# while success:
    # videoWrite.write(frame)
    # success, frame = videoCapture.read()

# cameraCapture=cv2.VideoCapture(0)
# fps = 30
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        # int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videoWrite = cv2.VideoWriter('C://Users//zy//Desktop//notepad++//zy66.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)

# success, frame = cameraCapture.read()
# numFramesRemaining=10*fps-1
# while success and numFramesRemaining > 0:
    # videoWrite.write(frame)
    # success, frame = cameraCapture.read()
    # numFramesRemaining=numFramesRemaining-1
# cameraCapture.release()



# clicked = False
# def onMouse(event,x,y,z,flags,param):
    # global clicked
    # if event == cv2.EVENT_LBUTTONUP:
        # cilcked = Ture
# cameraCapture = cv2.VideoCapture(0)
# cv2.namedWindow('myWindows')
# cv2.setMouseCallback('myWindows',onMouse)

# success, frame = cameraCapture.read()
# while success and cv2.waitKey(1) == -1 and not clicked:
    # cv2.imshow('myWindows',frame)
    # success, frame = cameraCapture.read()
# cv2.destroyWindow('myWindows')
# cameraCapture.release()

kernel_3x3 = np.array([[-1,-1,-1],
                      [-1, 8,-1],  
                      [-1,-1,-1]])
kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                      [-1,-1, 2,-1,-1],
                      [-1, 2, 4, 2,-1],
                      [-1,-1, 2,-1,-1],
                      [-1,-1,-1,-1,-1]])
                      
img = cv2.imread('C://Users//zy//Desktop//notepad++//zy.jpg',0)


k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)
blurred = cv2.GaussianBlur(img,(11,11),0)
g_hpf=img-blurred
cv2.imshow('3x3',k3)
cv2.imshow('5x5',k5)
cv2.imshow('g_hpf',g_hpf)
cv2.waitKey(0)
