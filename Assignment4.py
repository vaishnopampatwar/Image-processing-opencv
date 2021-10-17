import cv2
import numpy as np

img = cv2.imread('Image/obama.jpg', 1)
print(img.shape)
sp = 0.50
width = int(img.shape[1] * sp)
height = int(img.shape[0] * sp)
dim = (width, height)

res = cv2.resize(img, dim)
print(res.shape)
cv2.imshow('Input', img)
cv2.imshow('output', res)

rows, cols, ht = img.shape
##### TASK 2 #####
matrix = cv2.getRotationMatrix2D((rows / 2, cols / 2), 60, 0.7)
nimg = cv2.warpAffine(img, matrix, (cols, rows))
cv2.imshow('Input', img)
cv2.imshow('Rotation', nimg)

##### TASK 3 #####
matrix = np.float32([[1, 0, 100], [0,1, 100]])
nim = cv2.warpAffine(img, matrix, (640, 480))
cv2.imshow('Input', img)
cv2.imshow('output', nim)



##### TASK 4 #####
sp = 0.50
width = int(img.shape[1] * sp)
height = int(img.shape[0] * sp)
dim = (width, height)
res = cv2.resize(img, dim)
matrix = np.float32([[1, 0, 100], [0,1, 100]])
nim = cv2.warpAffine(res, matrix, (640, 480))
cv2.imshow('Input', img)
cv2.imshow('output', nim)

##### TASK 5 #####
im1 = cv2.imread('Image/im1.png', 1)
im3=im1+im1
cv2.imshow('output', im3)

im2 = cv2.imread('Image/im2.png', 1)
im3=im1+im2
cv2.imshow('Input1', im1)
cv2.imshow('Input2', im2)
cv2.imshow('output', im3)

##### TASK 6 #####
i1 = cv2.imread('Image/donald trump.jpg', 1)
i2 = cv2.imread('Image/jeff.jpg', 1)
img4 = cv2.bitwise_and(i1, i2)
cv2.imshow('Anding', img4)



cv2.waitKey(0)
cv2.destroyAllWindows()
