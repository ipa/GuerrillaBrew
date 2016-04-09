#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import time
import sched
from ui.MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    print(time.time())
    # s = sched.scheduler(time.time, time.sleep)
    # s.enter(2, 5, window.updatelcd, (s,))
    # s.run()
    #Timer(1, window.updatelcd).start()
    # timer = QTimer()
    # timer.setSingleShot(False)
    # m = QMetaMethod(window.updatelcd)
    # timer.connectNotify(m)
    # timer.start(1000)

    sys.exit(app.exec_())