#!/usr/bin/env python

import csv
from util.Observer import Observer
from datetime import datetime


class FileLogger:

    def __init__(self, filename):
        self.temperatureObserver = FileLogger.TemperatureObserver(self)
        self.currentSensorData = {'Name': None, 'Time': datetime.now(), 'Temperature': 0}
        self.filename = filename
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.currentSensorData.keys())

    def writeToFile(self):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.currentSensorData.values())
            # print('csv: ' + str(self.currentSensorData.values()))

    class TemperatureObserver(Observer):
        def __init__(self, outer):
            self.outer = outer

        def update(self, observable, arg):
            name, __, temperature = arg
            self.outer.currentSensorData['Time'] = datetime.now().strftime('%x %X')
            self.outer.currentSensorData['Temperature'] = temperature
            self.outer.currentSensorData['Name'] = name
            self.outer.writeToFile()
            pass
