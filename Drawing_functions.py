import numpy as mp

import  cv2
import numpy as np

img = cv2.imread('board.jpg' , 0)    #o for gray scale , 1 for RGB

#img = np.zeros([512 , 512 , 3 ])

img = cv2.line(img,(0,0) , (255,255) , (255, 0 , 0) , 10)   #search for other colors 
img = cv2.arrowedLine(img , (0,255) , (255, 255 ) , (255, 0 , 0) , 10 )

img = cv2.rectangle(img , (385 , 0) , (510 , 128) , (0 , 0 , 255) , 1)  #rectangle drawing
img = cv2.circle(img , (445 , 64) , 65 , ( 0 ,255 , 0 ) ,-1 )

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img , 'THA' , (10 , 500) , font , 4 , (255 , 255 , 255) , 10 , cv2.LINE_AA )


cv2.imshow('image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()

