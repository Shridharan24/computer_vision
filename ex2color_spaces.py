#RGB to BGR
import cv2
image = cv2.imread("C:/Users/student/Downloads/download.jfif")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RGB to HSV
import cv2
image = cv2.imread("C:/Users/student/Downloads/images.jfif")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#BGR to RGB
import cv2
image = cv2.imread("C:/Users/student/Pictures/Screenshots/bgr.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RGB to GRAY
import cv2
image = cv2.imread("C:/Users/student/Downloads/images.jfif")
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RGB to YUV
import cv2
image = cv2.imread("C:/Users/student/Downloads/images.jfif")
image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


