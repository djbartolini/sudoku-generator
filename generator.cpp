//
// Created by Daniel Bartolini on 5/7/24.
//

#include "generator.h"

const int MAX_NUM = 9;

//
// Generate random numbers from 1 to 9
//

int Generator::getRandomNum()
{
    int randomNum = std::rand()%MAX_NUM;
    return randomNum;
}

void Generator::createSeed()
{
    int randomNum = getRandomNum();
    std::cout << "RandomNum: " << randomNum << std::endl;
}

Generator::Generator()
{
    gridStatus = true;
}