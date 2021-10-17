import cv2
import numpy as np


def threshholdi_method(img):
    mat , th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('Th_in', img)
    cv2.imshow('Th_out', th)


def contrast_method(img):
    original = img.copy()
    xp = [0, 64, 128, 192, 255]
    fp = [0, 16, 128, 240, 255]
    x = np.arange(256)
    table = np.interp(x, xp, fp).astype('uint8')
    img = cv2.LUT(img, table)
    cv2.imshow("cs_in", original)
    cv2.imshow("cs_out", img)


imageFileName = input("enter the name of the image file: ")
img = cv2.imread(imageFileName)
choice = input("enter your choice : ")

print(choice)
if (choice == "1"):
    threshholdi_method(img)
# elif (choice == "2"):
#     contrast_method(img)
else:
    contrast_method(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
