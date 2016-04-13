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

    def update_not_working(self):
        QTimer().singleShot(2000, Timers().update_not_working)
        print('update')


def update_working():
    QTimer().singleShot(2000, update_working)
    print('update working')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('start timer')
    Timers().update_not_working()
    update_working()

    sys.exit(app.exec_())
