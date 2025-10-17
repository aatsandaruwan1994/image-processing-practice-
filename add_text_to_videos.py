import cv2
import datetime



cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3 , 700)
cap.set(4 , 700)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        
         font = cv2.FONT_HERSHEY_SIMPLEX
         text = 'width : ' + str(cap.get(3)) + 'Height:' + str(cap.get(4))
         datet = str(datetime.datetime.now())
         frame = cv2.putText(frame , text +  datet, (10 , 50 ) , font , 1 ,(0 ,255 ,255 ), 2 , cv2.LINE_AA)
         
         
         #gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # disable if not using gray scale video
         #cv2.imshow('frame', gray)
         cv2.imshow('frame' , frame)  # if we write frame except gray we can have RGB video
         
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    else :
        break
cap.release()
cv2.destroyAllWindows()



