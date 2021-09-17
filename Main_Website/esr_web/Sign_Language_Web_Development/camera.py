#imported necessary libraries
import cv2
from keras.models import load_model
import numpy as np
signModel=load_model(r'sign_lang_recog_train_model3.h5')
def letter(r):
    dic={0: 'Blank',1: 'A',2: 'B',3: 'C',4: 'D',5: 'E',6: 'F',7: 'G',8: 'H',9: 'I',10: 'J',11: 'K',12: 'L',13: 'M',14: 'N',15: 'O',16: 'P',17: 'Q',18: 'R',19: 'S',20: 'T',21: 'U',22: 'V',23: 'W',24: 'X',25: 'Y',26: 'Z'}
    return dic[r]
    
cap = cv2.VideoCapture(0) #camera acessing



class Video_Sign(object):
    def __init__(self):
         self.cap = cv2.VideoCapture(0) #camera acessing
    def __del__(self):
       self.cap.release()
    
    def get_frame(self):
        def letter(r):
            dic={0: 'Blank',1: 'A',2: 'B',3: 'C',4: 'D',5: 'E',6: 'F',7: 'G',8: 'H',9: 'I',10: 'J',11: 'K',12: 'L',13: 'M',14: 'N',15: 'O',16: 'P',17: 'Q',18: 'R',19: 'S',20: 'T',21: 'U',22: 'V',23: 'W',24: 'X',25: 'Y',26: 'Z'}
            return dic[r]
        _, frame = self.cap.read()
        if not _:
           print("Oops! looks like I don't have access to your camera :-(") #unble to access camera error message
    # Simulating mirror image
        frame = cv2.flip(frame, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        roi = cv2image[y1:y2, x1:x2]
#     roi=cv2.flip(roi,1)
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),2)
        th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        test_image=cv2.resize(res,(128,128))
        cv2.imshow("test",test_image)
        result=signModel.predict(test_image.reshape(1, 128, 128, 1))
        rounded_predictions=np.argmax(result,axis=-1)
#     print(rounded_predictions[0])
        cv2.putText(frame,str(letter(rounded_predictions[0])),(80,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        cv2.imshow('Sign Language Recognisation', frame)
        _,jpg=cv2.imencode(".jpg",frame)
        return jpg.tobytes()