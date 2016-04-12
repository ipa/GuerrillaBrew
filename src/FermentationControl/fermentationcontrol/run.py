#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from sensors.TemperatureSensor import  TemperatureSensor
from fcio.FileLogger import FileLogger


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    filelogger = FileLogger('output.log')
    tsensor = TemperatureSensor('23')
    tsensor.tempChangedNotifier.addObserver(window.temperatureObserver)
    tsensor.tempChangedNotifier.addObserver(filelogger.temperatureObserver)
    tsensor.update()

    sys.exit(app.exec_())

