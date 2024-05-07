#!/usr/bin/env python3

import os
import platform

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Compiling project . . . . . .")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Compile command
compile_line = os.system("clang++ -o sudoku-generator.exe main.cpp generator.cpp")

# Compile flag
if compile_line == 0:
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("Compiled successfully")
    print("~~~~~~~~~~~~~~~~~~~~~")

    # Determining platform
    namestr = platform.system()

    if namestr == 'Linux':
        platform = 'linux'

    elif namestr == 'Darwin':
        platform = 'macos'

    # Command alias
    alias_line = f"alias generate='{os.path.abspath('sudoku-generator.exe')}'"

    shell_profile = os.path.expanduser("~/.bashrc" if platform == 'linux' else "~/.bash_profile")
    if not any("sudoku-generator" in line for line in open(shell_profile)):
        with open(shell_profile, "a") as profile:
            profile.write(alias_line + "\n")
