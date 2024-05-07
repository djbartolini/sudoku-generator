#!/usr/bin/env python3

import os
import platform

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Compiling project . . . . . .")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Compile command
compile_command = os.system("clang++ -o sudoku-generator.exe main.cpp generator.cpp")

if compile_command == 0:
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Compiled successfully")
    print("~~~~~~~~~~~~~~~~~~~~~")
