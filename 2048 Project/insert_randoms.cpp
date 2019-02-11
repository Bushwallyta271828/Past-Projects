#include "insert_randoms.hpp"
#include <vector>
#include <ctime> //used in randomness
#include <cstdlib> //used in randomness

void insert_randoms(char* board)
{
    /*
     This function randomly inserts
     the 2 or the 4 into the blank spaces
     of board.
     */
    std::vector<int> zeroes;
    zeroes.reserve(16);
    for (int i = 0; i < 16; ++i)
    {
        if (board[i] == 0)
        {
            zeroes.push_back(i);
        }
    }
    if (zeroes.size() > 0)
    {
        int pos = std::rand() % zeroes.size();
        if (std::rand() % 100 < PROB * 100)
        {
            board[zeroes[pos]] = 2;
        }
        else
        {
            board[zeroes[pos]] = 1;
        }
    }
}
