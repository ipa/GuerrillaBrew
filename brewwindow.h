#ifndef BREWWINDOW_H
#define BREWWINDOW_H

#include <QDialog>

namespace Ui {
class BrewWindow;
}

class BrewWindow : public QDialog
{
    Q_OBJECT

public:
    explicit BrewWindow(QWidget *parent = 0);
    ~BrewWindow();

private slots:
    void on_stopButton_clicked();

private:
    Ui::BrewWindow *ui;
};

#endif // BREWWINDOW_H
