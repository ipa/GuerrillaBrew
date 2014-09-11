#include "mainwindow.h"
#include <QApplication>
#include <boost/date_time/gregorian/gregorian.hpp>

using namespace boost::gregorian;

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    // The following date is in ISO 8601 extended format (CCYY-MM-DD)
    std::string s("2001-10-20");
    date d(from_simple_string(s));
    std::cout << to_simple_string(d) << std::endl;

    return a.exec();
}
