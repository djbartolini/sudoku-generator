
#include "generator.h"

int main()
{
    // TODO: Step 1 - create instance of Generator
    //                Create Generator class
    //                Include it
    Generator* sudokuPuzzle = new Generator();

    sudokuPuzzle->createSeed();

    // TODO: Step 2 - create seed for puzzle generator
    //                write generateSeed() method

    // TODO: Step 3 - Generate the puzzle using method
    //                from Sudoku class
    //                generatePuzzle() method

    // TODO: Step 4 - Print the puzzle to the CLI
    //                printGrid() method


    delete sudokuPuzzle;

    return 0;
}