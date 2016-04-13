#!/usr/bin/env python

from util.Observer import Observer
from datetime import datetime


class ConsoleLogger:
    def __init__(self):
        self.temperatureObserver = ConsoleLogger.TemperatureObserver(self)
        self.currentSensorData = {'Name': None, 'Time': datetime.now(), 'Temperature': 0}

    def writeToConsole(self):
        print(self.currentSensorData, 'foo')

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            name, now, temperature = arg
            self.outer.currentSensorData['Time'] = datetime.now().strftime('%x %X')
            self.outer.currentSensorData['Temperature'] = temperature
            self.outer.currentSensorData['Name'] = name
            self.outer.writeToConsole()
            pass
