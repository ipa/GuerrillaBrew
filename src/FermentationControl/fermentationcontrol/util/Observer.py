#!/usr/bin/env python


class Observer:
    def update(self, observable, arg):
        pass


class Observable:
    def __init__(self):
        self.observers = []
        self.changed = False

    def addObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self, arg = None):
        try:
            if not self.changed:
                return
            localArray = self.observers[:]
            self.clearChanged()
        finally:
            pass

        for observer in localArray:
            observer.update(self, arg)

    def deleteObservers(self):
        self.observers = []

    def setChanged(self):
        self.changed = True

    def clearChanged(self):
        self.changed = False

    def hasChanged(self):
        return self.changed

    def countObservers(self):
        return len(self.observers)
