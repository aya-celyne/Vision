import cv2
import math

img_path = "im1.jpg"
image_c = cv2.imread(img_path)
image = cv2.cvtColor(image_c,cv2.COLOR_BGR2GRAY)

#first convolution
blur_img = cv2.GaussianBlur(image, (5,5),5.0,0, cv2.BORDER_DEFAULT)
 
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image1.png", blur_img)
cv2.waitKey(0)

#second convolution
blur_img = cv2.GaussianBlur(blur_img, (5,5),100.0,0, cv2.BORDER_DEFAULT)
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image2.png", blur_img)
cv2.waitKey(0)

#third convolution
blur_img = cv2.GaussianBlur(blur_img, (5,5),200.0,0, cv2.BORDER_DEFAULT)
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image3.png", blur_img)
cv2.waitKey(0)

#fourth convolution
blur_img = cv2.GaussianBlur(blur_img, (5,5),300.0,0, cv2.BORDER_DEFAULT)
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image4.png", blur_img)
cv2.waitKey(0)

#fifth convolution
blur_img = cv2.GaussianBlur(blur_img, (5,5),400.0,0, cv2.BORDER_DEFAULT)
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image5.png", blur_img)
cv2.waitKey(0)

#fifth convolution
blur_img = cv2.GaussianBlur(blur_img, (5,5),500.0,0, cv2.BORDER_DEFAULT)
cv2.imshow('Blur image',blur_img)
cv2.imwrite("image6.png", blur_img)
cv2.waitKey(0)

#calculate differences 
img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.png')
img3 = cv2.imread('image3.png')
img4 = cv2.imread('image4.png')
img5 = cv2.imread('image5.png')
img6 = cv2.imread('image6.png')

first = img1 - img2
second = img3 - img4
third = img5 - img6

#show 
cv2.imshow('Difference Image 1', first)
cv2.imshow('Difference Image 2', second)
cv2.imshow('Difference Image 3', third)
cv2.waitKey(0)
cv2.destroyAllWindows()