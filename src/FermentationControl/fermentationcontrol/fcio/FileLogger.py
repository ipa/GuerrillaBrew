#!/usr/bin/env python

import csv
from util.Observer import Observer
from datetime import datetime

class FileLogger:

    def __init__(self, filename):
        self.temperatureObserver = FileLogger.TemperatureObserver(self)
        self.currentSensorData = {'Temperature': 0, 'Humidity': 0}
        self.filename = filename

    def writeToFile(self):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.currentSensorData.values())

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            # TODO: write to file
            self.outer.currentSensorData['Temperature'] = arg
            self.outer.writeToFile()
            pass
