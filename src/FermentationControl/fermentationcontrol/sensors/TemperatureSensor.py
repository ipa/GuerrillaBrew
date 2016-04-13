#!/usr/bin/env python

import os
import glob
import time
import random

from datetime import datetime
from util.Observer import Observable
from util.Config import Config
from PyQt5.QtCore import QTimer


class TemperatureSensor:

    def __init__(self, port, name, sensor):
        self.tempChangedNotifier = TemperatureSensor.TemperatureChangedNotifier(self)
        self.temperature = 0.0
        self.port = None
        self.name = None
        self.port = port
        self.name = name
        self.sensor = sensor

    @staticmethod
    def create_sensor(sensor_config):
        sensor_name, sensor_type, sensor_port = sensor_config

        switcher = {
            'DS18B20': DS18B20([sensor_port]),
            'DummySensor': DummySensor(sensor_config),
        }
        sensor = switcher.get(sensor_type, None)
        sensor.connect()
        ts = TemperatureSensor(sensor_port, sensor_name, sensor)

        return ts

    @staticmethod
    def create_sensors_from_list(sensor_config):
        sensors = []
        for sensor_name in sensor_config:
            sc = sensor_config[sensor_name]
            sensor_type = sc[1]
            sensor_port = sc[0]
            ts = TemperatureSensor.create_sensor([sensor_name, sensor_type, sensor_port])
            sensors.append(ts)

        return sensors

    def changeValue(self, t):
        self.temperature = t
        self.tempChangedNotifier.notify()

    def update(self):
        QTimer().singleShot(Config().get_sensor_interval(), self.update)
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
            self.notifyObservers([self.outer.name, datetime.now(), self.outer.temperature])


class Sensor:
    def __init__(self, args=None):
        print(args)
        pass

    def connect(self):
        pass

    def read_value(self):
        pass


class DummySensor(Sensor):
    def __init__(self, args=None):
        Sensor.__init__(self, args)

    def connect(self):
        print('Connected')

    def read_value(self):
        Sensor.read_value(self)
        return 20.0 + random.uniform(-2, 2)


class DS18B20(Sensor):

    def __init__(self, args=None):
        Sensor.__init__(self, args)
        try:#sudo -S
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')
        except PermissionError as pe:
            print('Could not initialize w1-gpio, w1-therm', pe)

        self.device_file = None
        self.port_name = args[0]

    def connect(self):
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + self.port_name)[0] # '28*'
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

