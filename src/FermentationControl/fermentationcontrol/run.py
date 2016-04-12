#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from ui.MainWindow import MainWindow
from sensors.TemperatureSensor import  TemperatureSensor
import sched, time
from timers import Timers
from fcio.FileLogger import FileLogger

def foo():
    QTimer().singleShot(1000, foo)
    print('Foo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    filelogger = FileLogger('output.log')
    tsensor = TemperatureSensor('23')
    tsensor.tempChangedNotifier.addObserver(window.temperatureObserver)
    tsensor.tempChangedNotifier.addObserver(filelogger.temperatureObserver)
    tsensor.update()

    # Timers().add_sensor('Temperature', tsensor)
    # Timers().start()

    sys.exit(app.exec_())

