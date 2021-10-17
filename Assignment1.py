import cv2
# a.Read Image
img=cv2.imread('Image/elon_musk.jpg', cv2.IMREAD_COLOR)

# b.Display Image
cv2.imshow('elon musk',img)

# c.Display size of image
print('Image Dimension    : ',img.shape)

# Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
print('Image Height         : ',img.shape[0])

# Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
print('Image Width        : ',img.shape[1])

# Number of Channels represents the number of components used to represent each pixel.
print('Number of Channels : ',img.shape[2])

# d.Read the gray level value of a pixel at given coordinate
(b, g, r) = img[50, 50]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r,g,b))

# e.Resize image and save it
bigger = cv2.resize(img, (1050, 910))
cv2.imshow('Rsized ',bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()