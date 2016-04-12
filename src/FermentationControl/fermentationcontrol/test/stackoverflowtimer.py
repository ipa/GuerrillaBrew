#!/usr/bin/env python

import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication


class Borg():
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Timers(Borg):

    def __init__(self):
        Borg.__init__(self)

    def start(self):
        self.update()

    def update(self):
        QTimer().singleShot(2000, Timers().update)
        print('update')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('start timer')
    Timers().start()

    sys.exit(app.exec_())
