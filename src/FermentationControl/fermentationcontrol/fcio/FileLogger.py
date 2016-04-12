#!/usr/bin/env python

import csv
from util.Observer import Observer
import os.path
from datetime import datetime

class FileLogger:

    def __init__(self, filename):
        self.temperatureObserver = FileLogger.TemperatureObserver(self)
        self.currentSensorData = {'Time': datetime.now(), 'Temperature': 0, 'Humidity': 0}
        self.filename = filename
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.currentSensorData.keys())

    def writeToFile(self):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.currentSensorData.values())

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            now, temperature = arg
            self.outer.currentSensorData['Time'] = now
            self.outer.currentSensorData['Temperature'] = temperature
            self.outer.writeToFile()
            pass
