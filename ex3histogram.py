#HISTOGRAM EQUALIZATION &MAPPING

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('C:/Users/student/Downloads/download.jfif', 0)
equ = cv2.equalizeHist(img)
h=cv2.calcHist((img), [0], None, [256], [0,256])
h1=cv2.calcHist((equ), [0], None, [256], [0,256])
res = np.hstack((img, equ))
cv2.imshow('image.jpg', res)
plt.plot(h)
plt.plot(h1)
plt.title("Histogram Mapping & Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.grid()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


#STRECHING

import cv2
import numpy as np
img = cv2.imread('C:/Users/student/Downloads/download.jfif')
original = img.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
