import cv2

input = cv2.imread('C:/Users/student/Downloads/download.jfif')

height, width = input.shape[:2]

w, h = (256, 256)
a, b = (16,16)
c, d = (2, 2)

temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
temp1 = cv2.resize(input, (a, b), interpolation=cv2.INTER_LINEAR)
temp2 = cv2.resize(input, (c, d), interpolation=cv2.INTER_LINEAR)

#Initialize output image
 
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
output1 = cv2.resize(temp1, (width, height), interpolation=cv2.INTER_NEAREST)
output2 = cv2.resize(temp2, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow("8bit.jpg", output)
cv2.imshow("4bit.jpg",output2)
cv2.imshow("1bit.jpg",output3)
cv2.imshow("24bit.jpg",input)

#24 Bit to 8 Bit

import cv2
#Input image
input = cv2.imread('C:/Users/student/Downloads/download.jfif')
#Get input size
height, width = input.shape[:2]
w, h = (256, 256)
temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR)
output1 = cv2.resize(temp, (width, height), cv2.INTER_NEAREST)
cv2.imshow("8bit.jpg",output1)
cv2.imshow("24bit.jpg",input)

#24 Bit to 4 Bit

import cv2
#Input image
input = cv2.imread('C:/Users/student/Downloads/download.jfif')
#Get input size
height, width = input.shape[:2]
a, b = (16, 16)
temp1 = cv2.resize(input, (a, b), cv2.INTER_LINEAR)
output2 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST)
cv2.imshow("4bit.jpg",output2)
cv2.imshow("24bit.jpg",input)

#24 Bit to 1 Bit

import cv2
#Input image
input = cv2.imread('C:/Users/student/Downloads/download.jfif')
#Get input size
height, width = input.shape[:2]
c, d = (2, 2)
temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR)
output3 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST)
cv2.imshow("1bit.jpg",output3)
cv2.imshow("24bit.jpg",input)
