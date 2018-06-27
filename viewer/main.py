import sys
import numpy as np
import cv2
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QMainWindow, QDockWidget

from util import image_resize

class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()
    self._ui()

  def _ui(self):
    self.statusBar().showMessage('Read')
    self.imageScene = ImageViewer()
    self.setCentralWidget(self.imageScene)
    dock = QDockWidget('Controls', self)
    dock.setAllowedAreas(Qt.RightDockWidgetArea)
    self.addDockWidget(Qt.RightDockWidgetArea, dock)
    self.show()

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
      self.close()

class ImageViewer(QGraphicsView):

  def __init__(self):
    super(ImageViewer, self).__init__()
    self._ui()

  def _ui(self):
    self.scene = QGraphicsScene(self)
    
    image = cv2.imread('../equipment.jpg')
    image = image_resize(image, 1200)

    height, width, byteValue = image.shape
    byteValue = byteValue * width
    
    cv2.cvtColor(image, cv2.COLOR_BGR2RGB, image)
    
    self.qImage = QImage(image, width, height, byteValue, QImage.Format_RGB888)
    self.pixelMap = QPixmap.fromImage(self.qImage)
    self.viewItem = self.scene.addPixmap(self.pixelMap)

    self.setScene(self.scene)

  # def updateImage(self, qImage):
  #   value = qRgb(0, 0, 0)
  #   qImage.setColor(0, value)

  #   value = qRgb(255, 255, 255)
  #   qImage.setColor(1, value)

  #   pixMap = QPixmap.fromImage(qImage)

  #   self.viewItem.setPixmap(pixMap)
  #   self.viewItem.setPos(0, 0)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    window.setWindowTitle('Simple')
    sys.exit(app.exec_())
