from predic import *
from takePhoto import *

class Main:
    def __init__(self) -> None:
        self.getName = ""
    
    def getData(self):
        getModel = PredicData()
        self.getName = getModel.sendData()
        print(self.getName)
    
    def capture(self):
        openCam = TakePhoto()
        openCam.takePicture()

    
