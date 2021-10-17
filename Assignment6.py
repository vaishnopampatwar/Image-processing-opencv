import cv2

#Read the image 
img = cv2.imread('Image/obama.jpg',)

img_laplacian1 = cv2.Laplacian(img,0,ksize=1)
img_laplacian2 = cv2.Laplacian(img,0,ksize=3)
img_sharpened = cv2.add(img,img_laplacian2)

cv2.imshow('Input'  ,img)
cv2.imshow('Output1',img_laplacian1)
cv2.imshow('Output2',img_laplacian2)
cv2.imshow('Sharp',img_sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()