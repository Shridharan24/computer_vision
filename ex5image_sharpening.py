import cv2 
import sys 
import numpy as np 
image = cv2.imread("C:/Users/student/Desktop/Grapes-Blog-Image.jpg") 
if image is None: 
    print("can not find image") 
    sys.exit() 
sharpeningKernel = np.array(([0, -1, 0],[-1, 5, -1],[0, -1, 0]), dtype="int") 
output = cv2.filter2D(image, -1, sharpeningKernel) 
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE) 
cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE) 
cv2.imshow("image", image) 
cv2.imshow("output", output) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
