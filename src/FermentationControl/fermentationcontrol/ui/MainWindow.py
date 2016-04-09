#!/usr/bin/env python

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    lcdvalue = 20.0

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.show()
        self.closeButton.clicked.connect(self.onClose)
        self.updatelcd()

    def updatelcd(self):
        self.lcdvalue += 0.1
        self.lcdNumber.display(self.lcdvalue)
        #sc.enter(2, 1, self.updatelcd, (sc,))
        print("foo")

    def onClose(self):
        self.close()
        sys.exit(0)
