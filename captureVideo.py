from picamera import PiCamera
from datetime import datetime, time

class CaptureVideo:
    def __init__(self):
        self.camera = PiCamera()
        self.resolution = (640, 480)

    def record(self, fileName=None, durationInSeconds=10):
        if fileName is None:
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y-%H:%M:%S")
            fileName = 'video-{}.h264'.format(dt_string)
        if self.isDark():
            self.camera.brightness = 55
        else:
            self.camera.brightness = 50
        self.camera.start_recording(fileName)
        self.camera.wait_recording(durationInSeconds)
        self.camera.stop_recording()
    
    def isDark(self):
        now = datetime.now()
        nowTime = now.time()
        if nowTime >= time(18,00) or nowTime <= time(7,00):
            return True
        return False

captureVideo = CaptureVideo()
captureVideo.record(None)