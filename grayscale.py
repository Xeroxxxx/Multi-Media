import cv2
import numpy as np

# Read the original image
img = cv2.imread('raiden.jpg')

# Display the original image
cv2.imshow('Original', img)

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a new image with three channels, each containing the grayscale values
img2 = np.zeros_like(img)
img2[:, :, 0] = gray_image
img2[:, :, 1] = gray_image
img2[:, :, 2] = gray_image

# Display the grayscale image with three channels
cv2.imshow('Grayimage', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
