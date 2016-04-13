#!/usr/bin/env python

import sys
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from util.Observer import Observer
from util.Config import Config

class MainWindowControl:
    def __init__(self):
        pass


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.show()
        # self.showFullScreen()
        self.initSignals()
        self.temperatureObserver = MainWindow.TemperatureObserver(self)

    def initSignals(self):
        self.closeButton.clicked.connect(self.onClose)

    def updatelcd(self, lcdvalue):
        disp = '{0:.2f}'.format(lcdvalue)
        self.lcdNumber.display(disp)
        self.labelLast.setText('Last Update: ' + datetime.now().strftime('%x %X'))

    def onClose(self):
        self.close()
        sys.exit(0)

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            # print(arg)
            name, __, val = arg
            if Config().get_display_sensor() == name:
                self.outer.updatelcd(val)
            # print(self.outer)


