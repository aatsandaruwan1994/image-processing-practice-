import numpy as np
import cv2


def click_event(event, x, y, flags, param):  # parameters
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img , (x , y) , 3 ,(0 , 0 , 255) , -1 )
        mycolorImage = np.zeros((512 , 512 , 3) , np.uint8)
        
        mycolorImage[:] = [blue , green , red]
        cv2.imshow('image', mycolorImage)


#img = np.zeros((512, 512, 3), np.uint8) #create black image using numpy
img = cv2.imread('board.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
