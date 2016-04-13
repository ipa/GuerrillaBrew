#!/usr/bin/env python

import os
import glob
import time
import random

from datetime import datetime
from util.Observer import Observable
from PyQt5.QtCore import QTimer


class TemperatureSensor:

    def __init__(self, port):
        self.tempChangedNotifier = TemperatureSensor.TemperatureChangedNotifier(self)
        self.temperature = 20.0
        self.port = port
        self.sensor = DummySensor()

    def changeValue(self, t):
        self.temperature = t
        self.tempChangedNotifier.notify()

    def update(self):
        QTimer().singleShot(2000, self.update)
        self.changeValue(self.readFromSensor())

    def readFromSensor(self):
        val = self.sensor.read_value()
        return val

    class TemperatureChangedNotifier(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer

        def notify(self):
            self.setChanged()
            self.notifyObservers([datetime.now(), self.outer.temperature])


class Sensor:
    def __init__(self):
        pass

    def read_value(self):
        pass


class DummySensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)

    def read_value(self):
        Sensor.read_value(self)
        return 20.0 + random.uniform(-2, 2)


class DS18B20(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read_value(self):
        return self.read_temp()

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f

