#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "brewwindow.h"
namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void on_closeButton_clicked();

    void on_startBrew_clicked();

    void on_openBrew_clicked();

private:
    Ui::MainWindow *ui;
    BrewWindow *brewWindow;
};

#endif // MAINWINDOW_H
