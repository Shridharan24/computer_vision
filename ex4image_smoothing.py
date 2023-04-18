import cv2
import numpy as np
image = cv2.imread('C:/Users/student/Downloads/image.jfif')
averageBlur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow('Original', image)
cv2.imshow('Average blur', averageBlur)
cv2.imshow('Gaussian blur', gaussian)
cv2.waitKey()
cv2.destroyAllWindows()
