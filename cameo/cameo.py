import cv2
import filters
from managers import WindowManager, CaptureManager
class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.enterFrame
            filters.strokeEdges(frame,frame)
            self._curveFilter.apply(frame,frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    def onKeypress(self,keycode):
        if keycode == 32:  # space
            self._captureManager.writeImage('C://Users//zy//Desktop//notepad++//cameo//screenshot.png')
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('C://Users//zy//Desktop//notepad++//cameo//screenshot2.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:    # escape
            self._windowManager.destoryWindow()
if __name__ == "__main__":
    Cameo().run()

