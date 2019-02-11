#include "move.hpp"
#include "print_board.hpp"
#include "insert_randoms.hpp"
#include "done.hpp"
#include "find_direction.hpp"
#include <iostream> //used for printing
#include <ctime> //used in initializing randomness.
#include <cstdlib> //used in initializing randomness

int main()
{
    /*
     *See the README.txt file
     */
    std::srand(std::time(0));
    float coeffs[] = {1, 1, 1, 1};
    char board[16] = {0};
    insert_randoms(board);
    insert_randoms(board);
    int score = 0;
    print_board(board, score);
    char direction;
    while (done(board) == false)
    {
        std::cout << "\n\n";
        direction = find_direction(board, coeffs);
        std::cout << "direction = " << (int) direction << std::endl;
        score = move(board, score, direction);
        insert_randoms(board);
        print_board(board, score);
    }
    std::cout << "DONE" << std::endl;
}
