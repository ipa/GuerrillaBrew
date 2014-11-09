#-------------------------------------------------
#
# Project created by QtCreator 2014-09-08T19:04:14
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = GuerrillaBrew
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    brewwindow.cpp

HEADERS  += mainwindow.h \
    brewwindow.h

FORMS    += mainwindow.ui \
    brewwindow.ui

RESOURCES += \
    resources.qrc

OTHER_FILES += \
    LICENSE \
    README.md

## Libraries
INCLUDEPATH += /usr/local/Cellar/boost/1.55.0_2/include
LIBS += -L/usr/local/Cellar/boost/1.55.0_2/lib -lboost_date_time

