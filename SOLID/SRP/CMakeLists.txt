cmake_minimum_required(VERSION 3.10)
project(Sandpiles LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(sandpiles main.cpp)

if (UNIX)
    target_link_libraries(sandpiles stdc++fs)
endif()
