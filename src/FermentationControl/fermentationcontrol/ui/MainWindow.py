#!/usr/bin/env python

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from util.Observer import Observer


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.show()
        # self.showFullScreen()
        self.updatelcd(22.3)
        self.initSignals()
        self.temperatureObserver = MainWindow.TemperatureObserver(self)

    def initSignals(self):
        self.closeButton.clicked.connect(self.onClose)

    def updatelcd(self, lcdvalue):
        self.lcdNumber.display(lcdvalue)

    def onClose(self):
        self.close()
        sys.exit(0)

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            self.outer.updatelcd(arg)
            # print(self.outer)


