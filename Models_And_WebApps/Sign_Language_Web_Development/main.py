#imported necessary libraries
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
model=load_model(r'sign_lang_recog_train_model.h5')
def letter(r):
    dic={0: 'Blank',1: 'A',2: 'B',3: 'C',4: 'D',5: 'E',6: 'F',7: 'G',8: 'H',9: 'I',10: 'J',11: 'K',12: 'L',13: 'M',14: 'N',15: 'O',16: 'P',17: 'Q',18: 'R',19: 'S',20: 'T',21: 'U',22: 'V',23: 'W',24: 'X',25: 'Y',26: 'Z'}
    return dic[r]
    
cap = cv2.VideoCapture(0) #camera acessing
while True:
    _, frame = cap.read()
    labels = []
    if not _:
        print("Oops! looks like I don't have access to your camera :-(") #unble to access camera error message
        break
        
    
    cv2.rectangle(frame, (320,100),(620, 400), (255,0,0),5)
    roi=frame[100:400,320:620]
    roi=cv2.flip(roi, 1)
    #cv2.imshow('roi',roi)
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi=cv2.resize(roi,(128,128),interpolation =cv2.INTER_AREA)
    roi = roi.astype('float')/255.0
    roi = img_to_array(roi)
    #cv2.imshow('roi sacled and gray', roi)
    
    roi= roi.reshape(1,128,128,1)    #128*128
    result = model.predict(roi)[0]
    #print(result)
    result=list(result)
    result=int(result.index(max(result)))
    #print(type(result))
    #print(result)
    cv2.putText(frame,str(letter(result)),(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    cv2.imshow('Sign Language Recognisation', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit the camera window!
        break

cap.release()
cv2.destroyAllWindows()