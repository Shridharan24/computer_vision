import cv2
import numpy as np

#Haris Corner Detection

img = cv2.imread('chess.jpg')
image = cv2.imread('chess.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)

dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)

dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0,0,255]
Hori = np.concatenate((img, image), axis=1)
cv2.imshow('haris_corner', Hori)
cv2.waitKey()

#SIFT Detection

image = cv2.imread('chess.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray_image, None)

kp_image = cv2.drawKeypoints(image, kp, None, color=(
0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
Hori = np.concatenate((img, kp_image), axis=1)
cv2.imshow('SIFT', Hori)
cv2.waitKey()

#FAST

image = cv2.imread('chess.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)
kp = fast.detect(gray_image, None)
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 0,255))
Hori = np.concatenate((img, kp_image), axis=1)
cv2.imshow('FAST', Hori)
cv2.waitKey()
cv2.destroyAllWindows()
