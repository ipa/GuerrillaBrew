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
        self.current_display_sensor = Config().get_display_sensor()
        self.sensor_names = []
        sensors = Config().get_sensors()
        for sensor_name in sensors:
            self.sensor_names.append(sensor_name)

    def initSignals(self):
        self.closeButton.clicked.connect(self.onClose)
        self.toggleButton.clicked.connect(self.onNextSensor)

    def updatelcd(self, lcdvalue):
        disp = '{0:.2f}'.format(lcdvalue)
        self.lcdNumber.display(disp)
        self.labelLast.setText('Sensor: ' + self.current_display_sensor + '     '
                               'Last Update: ' + datetime.now().strftime('%x %X'))

    def onClose(self):
        self.close()
        sys.exit(0)

    def onNextSensor(self):
        idx = self.sensor_names.index(self.current_display_sensor)
        new_idx = (idx + 1) % len(self.sensor_names)
        self.current_display_sensor = self.sensor_names[new_idx]

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            name, __, val = arg
            if self.outer.current_display_sensor == name:
                self.outer.updatelcd(val)


