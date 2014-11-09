#include <iostream>
#include <boost/asio.hpp>
#include <boost/date_time/gregorian/gregorian.hpp>
#include <boost/date_time/posix_time/posix_time.hpp>

using namespace std;
using namespace boost::gregorian;

void print(const boost::system::error_code& )
{
    cout << "1 seconds later" << endl;
}

int main() {
    cout << "Hello, World!" << endl;

    cout << "Test boot..." << endl;

    // The following date is in ISO 8601 extended format (CCYY-MM-DD)
    std::string s("2001-10-20");
    date d(from_simple_string(s));
    std::cout << to_simple_string(d) << std::endl;

    // async timer
    cout << "test timer" << endl;
    boost::asio::io_service io1;
    boost::asio::deadline_timer t1(io1, boost::posix_time::seconds(1));
    t1.async_wait(print);
    io1.run();

    return 0;

}