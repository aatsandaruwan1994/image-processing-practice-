import cv2
cap = cv2.VideoCapture(0) #selecting the input source
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 480))   #save video clip


print(cap.isOpened())
while(True):
    ret , frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    #getting properties of video
        rint(cap.get(cv2.CAP_PROP_FRAME_))
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame' , frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):    #escape code
        break
        
cap.release()
cv2.destroyAllWindows()