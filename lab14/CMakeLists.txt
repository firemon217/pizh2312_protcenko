cmake_minimum_required(VERSION 3.12.0)
project(lab14 VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

link_directories(lib)

add_subdirectory(lib)
add_subdirectory(bin)

enable_testing()
add_subdirectory(tests)
