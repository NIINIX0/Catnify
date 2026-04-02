cmake_minimum_required(VERSION 3.5)
project(Catnify)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(EVERYTHING
main.cpp
)

add_executable(Catnify ${EVERYTHING})
