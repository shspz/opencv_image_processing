import cv2
import numpy as np

image = cv2.imread("D:\github\opencv_image_processing\moon.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()