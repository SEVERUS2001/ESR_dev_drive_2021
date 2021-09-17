# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:21:00 2021

@author: Happy
"""

from flask import  Flask, render_template,Response
from camera import Video_Emotion_1, Video_Sign, Video_Emotion_2


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')
def gen(camera):
    while True:
      frame=camera.get_frame()
      yield(b'--frame\r\n'
    b'Content-Type: image/jpeg\r\n\r\n'+frame+
    b'\r\n\r\n')
    

@app.route("/emotion_video_1")
def video_emotion_1():
    #return render_template('output.html')
    return Response(gen(Video_Emotion_1()), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/emotion_video_2")
def video_emotion_2():
    return Response(gen(Video_Emotion_2()), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/sign_video")
def sign_video():
    return Response(gen(Video_Sign()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=="__main__":
    app.run(debug=True, port=1000)