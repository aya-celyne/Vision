import cv2

img_path = "C:/Users/21354/Desktop/MIV/MIV S2/Vision/TP/TP1/im1.jpg"
image_c = cv2.imread(img_path)
image = cv2.cvtColor(image_c,cv2.COLOR_BGR2GRAY)

# Mentioning absolute path of the image
# cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
# borderType: This specifies the boundaries of an image while the kernel is applied to the borders of an image.
# cv2.BORDER_DEFAULT: gfedcb|abcdefgh|gfedcba

sigma1 = 4
sigma2 = 5
sigma = ((sigma1**2 + sigma2**2)**0.5)

# Compute the Gaussian kernel size based on sigma
ksize = int(2 * round(2 * sigma) + 1)

# Convolve with Gaussian kernel
g = cv2.GaussianBlur(image, (ksize, ksize), sigma1, borderType=cv2.BORDER_DEFAULT)

# Repeat n times
n = 4
for i in range(n):
    g = cv2.GaussianBlur(g, (ksize, ksize), sigma1, borderType=cv2.BORDER_DEFAULT)

# Convolve with Gaussian kernel again
g = cv2.GaussianBlur(g, (ksize, ksize), sigma2, borderType=cv2.BORDER_DEFAULT)

# Show the image on the newly created image window
cv2.imshow('Blur image', g)
cv2.imwrite("im1b.png", g)
cv2.waitKey(0)
