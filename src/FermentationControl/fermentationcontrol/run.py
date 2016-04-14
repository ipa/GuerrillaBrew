#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from sensors.TemperatureSensor import  TemperatureSensor
from fcio.FileLogger import FileLogger
from fcio.ConsoleLogger import ConsoleLogger
from util.Config import Config

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with_gui = sys.argv.count('--no-gui') == 0

    sensors_config = Config().get_sensors()
    sensors = TemperatureSensor.create_sensors_from_list(sensors_config)

    file_logger = FileLogger('output.log')
    console_logger = ConsoleLogger()

    # Start Updates
    for sensor in sensors:
        sensor.tempChangedNotifier.addObserver(file_logger.temperatureObserver)
        sensor.tempChangedNotifier.addObserver(console_logger.temperatureObserver)
        sensor.update()

    # Start GUI
    if with_gui:
        print('starting gui...')
        window = MainWindow()
        for sensor in sensors:
            sensor.tempChangedNotifier.addObserver(window.temperatureObserver)

    sys.exit(app.exec_())


