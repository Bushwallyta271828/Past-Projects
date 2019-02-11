#include "done.hpp"
#include "move.hpp"
#include <algorithm> // std::copy and std::equal

bool done(char* board)
{
    /*
     *This function determines
      whether the game is over.
     *It takes as input the board
      and returns a bool value.
     *If the bool returned is true, then
      the game is over.
     *If the bool returned is false, then
      the game continues.
     */
    char new_board[16];
    std::copy(board, board + 16, new_board);
    bool same;
    for (char direction = 0; direction < 4; ++direction)
    {
        move_no_score(new_board, direction);
        same = std::equal(new_board, new_board + 16, board);
        if (!same) {return false;}
    }
    return true;
}
