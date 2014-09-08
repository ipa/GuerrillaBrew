#include <QApplication>
#include <QMessageBox>
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
//    QPixmap bkgnd("/Users/Iwan/Downloads/logo_with_homebrew.png");
//    bkgnd = bkgnd.scaled(this->size(), Qt::IgnoreAspectRatio);
//    QPalette palette;
//    palette.setBrush(QPalette::Background, bkgnd);
//    this->setPalette(palette);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_closeButton_clicked()
{
     QApplication::quit();
}

void MainWindow::on_startBrew_clicked()
{
    QMessageBox::information(NULL, "Start", "I'll start the brew, go and have a beer in the meanwhile!");
}
