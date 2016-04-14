#!/usr/bin/env python

import sys
import ast
from util.Borg import Borg
if sys.version < '3':
    import ConfigParser as configparser
else:
    import configparser


class Config(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.use_config = self.config.get('DEFAULT', 'UseConfig')

    def get_sensors(self):
        sensors = ast.literal_eval(self.config.get(self.use_config, 'Sensors'))
        return sensors

    def get_sensor_interval(self):
        return ast.literal_eval(self.config.get(self.use_config, 'SensorInterval'))

    def get_display_sensor(self):
        return self.config.get(self.use_config, 'DisplaySensor')
