import numpy as np
import cv2 as cv

img = cv.imread('im1.jpg')
#------------------------
# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# sift = cv.SIFT_create()
# kp = sift.detect(gray,None)
#--------------------------------
grayimage=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#create a sift object
siftobject=cv.SIFT_create()
keyp,dscrp=siftobject.detectAndCompute(grayimage,None)

#---------------

print(keyp[0].pt)
print(keyp[1].size)
print(keyp[11].angle)
print(keyp[0].response)
print(dscrp[12])

img=cv.drawKeypoints(grayimage,keyp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#img=cv.drawKeypoints(gray,kp,img)
#cv.imwrite('sift_keypoints.jpg',img)
# img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift_keypoints.jpg',img)