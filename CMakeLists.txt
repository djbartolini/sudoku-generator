cmake_minimum_required(VERSION 3.28)
project(sudoku_generator)

set(CMAKE_CXX_STANDARD 17)

add_executable(sudoku_generator main.cpp
        generator.cpp
        generator.h)
