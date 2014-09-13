#include "brewwindow.h"
#include "ui_brewwindow.h"
#include <QStandardItem>
#include <QStandardItemModel>

BrewWindow::BrewWindow(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::BrewWindow)
{
    ui->setupUi(this);
    QStandardItemModel* model = new QStandardItemModel();

    QStandardItem* item1 = new QStandardItem("Maltose Rest 55°");
    model->appendRow(item1);
    QStandardItem* item2 = new QStandardItem("Protein Rest °");
    model->appendRow(item2);

    ui->listView->setModel(model);
}

BrewWindow::~BrewWindow()
{
    delete ui;
}

void BrewWindow::on_stopButton_clicked()
{
    this->close();
}
