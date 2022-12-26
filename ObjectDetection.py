#Credits and Thanks
#https://github.com/opencv/opencv/tree/3.4/data/haarcascades
#https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python/
#https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

import cv2
  
class ObjectDetection:
    def __init__(self,cascade_classifier):
        self.haar_cascade = cv2.CascadeClassifier(cascade_classifier)
        self.cap = ""
    def load_entry(self,entry_type="webcam",image_path=""):
        entry = {}
        if entry_type == "image":
            entry['original'] = cv2.imread(image_path)
        elif entry_type == "webcam":
            if self.cap == "" or not self.cap.isOpened():
                self.cap = cv2.VideoCapture(0)
            ret, entry['original'] = self.cap.read()
            if entry['original'] is None:
                raise Exception("Webcam error...")
        entry['gray'] = cv2.cvtColor(entry['original'], cv2.COLOR_BGR2GRAY)
        return entry
    def detect(self, entry):
        rect = self.haar_cascade.detectMultiScale(entry['gray'])
        for (x, y, w, h) in rect:
            cv2.rectangle(entry['original'], (x, y), (x+w, y+h), (200, 0, 0), 1)
        cv2.imshow('Detections', entry['original'])
    def imageDetection(self, image_path):
        entry = self.load_entry("image",image_path)
        detection = self.detect(entry)
        cv2.waitKey(0)
    def webcamDetection(self):
        while True:
            entry = self.load_entry()
            detection = self.detect(entry)
            if cv2.waitKey(10) == 27:
                self.cap.release()
                break

objDetec = ObjectDetection(input("haarcascade path: "))
objDetec.imageDetection(input("image path: ")) if input("image or webcam?: ") == "image" else objDetec.webcamDetection()
