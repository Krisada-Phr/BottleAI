# from cv2 import *
import cv2 as cv
class TakePhoto:
    def __init__(self) -> None:
        pass

    def takePicture(self):
        cam_port = 0
        cam = cv.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv.imwrite("Bottle.png", image)
        else:
            print("No image detected. Please! try again")

if __name__ == "__main__":

    a = TakePhoto()
    a.takePicture()