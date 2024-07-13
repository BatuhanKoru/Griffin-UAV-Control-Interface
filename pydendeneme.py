
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from pydentasarlanan10 import Ui_MainWindow
import cv2

import numpy as np

import time

from PySide6.QtCore import QTimer, Qt

from PySide6.QtGui import QImage, QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.label.setGeometry()
        self.ui.webEngineView.setUrl(QUrl("https://maps.google.com/"))
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
