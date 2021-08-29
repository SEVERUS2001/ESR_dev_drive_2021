#imported necessary libraries
import cv2  # importing opencv
from deepface import DeepFace # import DeepFace

faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #haarcascade used for face recognisation




class Video(object):
    def __init__(self):
         self.cap = cv2.VideoCapture(0) #camera acessing
    def __del__(self):
       self.cap.release()
    def get_frame(self):
        _, frame = self.cap.read()
        if not _:
            print("Oops! looks like I don't have access to your camera :-(") #unble to access camera error message
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #conversion to gray scale as the model is trained in gray scale
        faces = faceCascade.detectMultiScale(gray) #face demensions
        try:
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0), 2) #drawing rectangle around face
                    result = DeepFace.analyze(frame, actions = ['emotion'])
                    label= result['dominant_emotion']
                    label_position=(x,y-20)
                    font = cv2.FONT_HERSHEY_SIMPLEX #chosing font
                    cv2.putText(frame,label,label_position, font, 1, (0,0,255),2) #writing text
                cv2.imshow('Emotion Detection', frame) #final show
                _,jpg=cv2.imencode(".jpg",frame)
                return jpg.tobytes()
        except:
                return "I can't detect your beautiful face! Sorry:-(!"
                return jpg.tobytes()
