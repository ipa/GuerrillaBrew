cmake_minimum_required(VERSION 2.8.4)
project(Brewcontrol)

# The version number.
set (Brewcontrol_VERSION_MAJOR 0)
set (Brewcontrol_VERSION_MINOR 1)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp PID.hpp PID.cpp)
add_executable(brewcontrol ${SOURCE_FILES})

set(Boost_USE_STATIC_LIBS        ON) # only find static libs
set(Boost_USE_MULTITHREADED      ON)
set(Boost_USE_STATIC_RUNTIME    OFF)
find_package(Boost 1.56.0 COMPONENTS date_time filesystem system timer)
if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
#  add_executable(foo foo.cc)
  target_link_libraries(brewcontrol ${Boost_LIBRARIES})
endif()