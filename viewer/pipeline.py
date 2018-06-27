# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2018-06-27 16:52:48
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2018-06-27 17:18:04

from PyQt5.QtCore import QObject, QThread

class CameraThread(QThread):
  def __init__(self, camera):
    QThread.__init__(self)
    self.camera = camera

  def __del__(self):
    self.wait()

  def run(self):
    img = next(self.camera)
    print(img.shape)

