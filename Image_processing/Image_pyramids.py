import cv2
import numpy as np


img = cv2.imread("messi5.jpg")

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrUp(img)

cv2.imshow("Original image" , img)
cv2.imshow("PyrD" , lr1)
cv2.imshow("PyrU" , lr2)

cv2.waitKey(0)
cv2.destroyAllWindows()