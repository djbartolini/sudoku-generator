//
// Created by Daniel Bartolini on 5/7/24.
//

// #ifndef SUDOKU_GENERATOR_GENERATOR_H
// #define SUDOKU_GENERATOR_GENERATOR_H

#include <iostream>
#include <stdio.h>
#include <cstdlib>

class Generator {
private:
    int grid[9][9];
    int randNums[9];

    bool gridStatus;

public:
    Generator();
    int getRandomNum();
    void createSeed();
    void generatePuzzle();
};

// #endif //SUDOKU_GENERATOR_GENERATOR_H
