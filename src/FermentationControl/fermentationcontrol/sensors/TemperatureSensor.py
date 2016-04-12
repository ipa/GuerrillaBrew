#!/usr/bin/env python

from util.Observer import Observable
from PyQt5.QtCore import QTimer


class TemperatureSensor:

    def __init__(self, port):
        self.tempChangedNotifier = TemperatureSensor.TemperatureChangedNotifier(self)
        self.temperature = 20.0
        self.port = port

    def changeValue(self, t):
        self.temperature = t
        self.tempChangedNotifier.notify()

    def update(self):
        QTimer().singleShot(100, self.update)
        self.changeValue(self.temperature + 0.1)

    def readFromSensor(self):
        # TODO: Read from sensor
        pass

    class TemperatureChangedNotifier(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notify(self):
            self.setChanged()
            self.notifyObservers(self.outer.temperature)


