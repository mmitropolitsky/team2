from analyzer.BaseAnalyzer import BaseAnalyzer
import cv2


class PostureAnalyzer(BaseAnalyzer):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # WIDTH
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # HEIGHT

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def has_exception(self):
        return not self.__is_person_in_frame()

    def __is_person_in_frame(self):
        ret, frame = self.cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        return bool(len(faces))
        # return False
