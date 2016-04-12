#!/usr/bin/env python

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from util.Borg import Borg
from sensors.TemperatureSensor import TemperatureSensor


class Timers(Borg):

    def __init__(self):
        Borg.__init__(self)
        if not hasattr(self, '_sensors'):
            self._sensors = {}

        self.stop = False
        self.temp = 20.1

    def add_sensor(self, sensorname, sensor):
        self._sensors[sensorname] = sensor

    def start(self):
        self.update()

    def update(self):
        QTimer().singleShot(2000, Timers().update)

        self.temp += 0.1
        self._sensors['Temperature'].changeValue(self.temp)
        print('Changed')

    def __str__(self):
        pass
