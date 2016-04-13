#!/usr/bin/env python

import configparser, ast
from util.Borg import Borg


class Config(Borg):

    def __init__(self):
        Borg.__init__(self)
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.use_config = 'DEVELOP' # TODO self.config.get('UseConfig')

    def get_sensors(self):
        sensors = ast.literal_eval(self.config[self.use_config]['Sensors'])
        return sensors

    def get_sensor_interval(self):
        return ast.literal_eval(self.config[self.use_config]['SensorInterval'])