#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from sensors.TemperatureSensor import  TemperatureSensor
from fcio.FileLogger import FileLogger
from util.Config import Config

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    filelogger = FileLogger('output.log')

    sensors_config = Config().get_sensors()
    sensors = TemperatureSensor.create_sensors_from_list(sensors_config)

    # Start Updates
    for sensor in sensors:
        sensor.tempChangedNotifier.addObserver(window.temperatureObserver)
        sensor.tempChangedNotifier.addObserver(filelogger.temperatureObserver)
        sensor.update()


    sys.exit(app.exec_())
