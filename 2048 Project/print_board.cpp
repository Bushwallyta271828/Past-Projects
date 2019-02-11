#include "print_board.hpp"
#include <iostream> //used for printing
#include <cmath> //used for finding the lengths of elements of the board

void print_board(char* char_board, int score)
{
    /*
     *This function prints the board
      in a reader-friendly manner and
      the score of the board along side it.
     */
    int board[16];
    for (int i = 0; i < 16; ++i)
    {
        if (char_board[i] == 0)
        {
            board[i] = 0;
        }
        else
        {
            board[i] = (1 << char_board[i]);
        }
    }
    int value;
    int max_length = 1;
    for (int i = 0; i < 16; ++i)
    {
        value = board[i];
        while (value > pow(10, max_length))
        {
            max_length++;
        }
    }
    int length;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            value = board[4*i + j];
            std::cout << value;
            if (value == 0)
            {
                for (int k = 0; k < max_length; ++k)
                {
                    std::cout << " ";
                }
            }
            else
            {
                length = 1;
                while (value > pow(10, length))
                {
                    length++;
                }
                for (int k = 0; k < (max_length - length + 1); ++k)
                {
                    std::cout << " ";
                }
            }
        }
        std::cout << '\n';
    }
    std::cout << "current score = " << score << std::endl;
}
