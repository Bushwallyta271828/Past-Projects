#include "move.hpp"
#include <iostream> //used in default clause to output error message.

int move(char* board, int score, char direction)
{
    /*
     *board points to a C-style array of 
      the elements of the grid.
     *score is the score of the game
     *direction specifies:
         0: right
         1: up
         2: left
         3: down
     *board is edited in place.
     *the new score is returned
     *in order to avoid copies, no pragma is used
     *all computation should be performed in one thread
      - move may be performed on several threads simultaneously, 
      but the same call won't be performed using more than one thread
     */
    switch(direction)
    {
        case 0:
            for (int row = 0; row < 4; ++row)
            {
                char* write_head = board + 4*row + 3;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + 4*row + 3;
                     position > board + 4*row -1;
                     position--)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head--;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            score += (1 << *write_head);
                            write_head--;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head--;
                }
                while (write_head > board + 4*row - 1)
                {
                    *write_head = 0;
                    write_head--;
                }
            }
            break;
        case 2:
            for (int row = 0; row < 4; ++row)
            {
                char* write_head = board + 4*row;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + 4*row;
                     position < board + 4*row + 4;
                     position++)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head++;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            score += (1 << *write_head);
                            write_head++;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head++;
                }
                while (write_head < board + 4*row + 4)
                {
                    *write_head = 0;
                    write_head++;
                }
            }
            break;
        case 1:
            for (int column = 0; column < 4; ++column)
            {
                char* write_head = board + column;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + column;
                     position < board + column + 16;
                     position += 4)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head += 4;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            score += (1 << *write_head);
                            write_head += 4;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head += 4;
                }
                while (write_head < board + column + 16)
                {
                    *write_head = 0;
                    write_head += 4;
                }
            }
            break;
        case 3:
            for (int column = 0; column < 4; ++column)
            {
                char* write_head = board + column + 12;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + column + 12;
                     position > board + column - 4;
                     position -= 4)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head -= 4;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            score += (1 << *write_head);
                            write_head -= 4;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head -= 4;
                }
                while (write_head > board + column - 4)
                {
                    *write_head = 0;
                    write_head -= 4;
                }
            }
            break;
        default:
            std::cout << "INVALID DIRECTION SPECIFIED FOR move!" << std::endl;
            std::cout << "direction specified: " << direction << "\n" << std::endl;
            break;
    }
    return score;
}


void move_no_score(char* board, char direction)
{
    /*
     *board points to a C-style array of 
      the elements of the grid.
     *direction specifies:
         0: right
         1: up
         2: left
         3: down
     *board is edited in place.
     *in order to avoid copies, no pragma is used
     *all computation should be performed in one thread
      - move may be performed on several threads simultaneously, 
      but the same call won't be performed using more than one thread
     *this variant of move should be used whenever the change in score
      is not needed - move_no_score is slightly faster than move.
     */
    switch(direction)
    {
        case 0:
            for (int row = 0; row < 4; ++row)
            {
                char* write_head = board + 4*row + 3;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + 4*row + 3;
                     position > board + 4*row -1;
                     position--)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head--;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            write_head--;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head--;
                }
                while (write_head > board + 4*row - 1)
                {
                    *write_head = 0;
                    write_head--;
                }
            }
            break;
        case 2:
            for (int row = 0; row < 4; ++row)
            {
                char* write_head = board + 4*row;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + 4*row;
                     position < board + 4*row + 4;
                     position++)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head++;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            write_head++;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head++;
                }
                while (write_head < board + 4*row + 4)
                {
                    *write_head = 0;
                    write_head++;
                }
            }
            break;
        case 1:
            for (int column = 0; column < 4; ++column)
            {
                char* write_head = board + column;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + column;
                     position < board + column + 16;
                     position += 4)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head += 4;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            write_head += 4;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head += 4;
                }
                while (write_head < board + column + 16)
                {
                    *write_head = 0;
                    write_head += 4;
                }
            }
            break;
        case 3:
            for (int column = 0; column < 4; ++column)
            {
                char* write_head = board + column + 12;
                bool accepting = true;
                char current_value = -1;
                for (char* position = board + column + 12;
                     position > board + column - 4;
                     position -= 4)
                {
                    if (*position != 0)
                    {
                        if (accepting)
                        {
                            accepting = false;
                            current_value = *position;
                        }
                        else if (current_value != *position)
                        {
                            *write_head = current_value;
                            write_head -= 4;
                            current_value = *position;
                        }
                        else // (accepting == false and current_value == *position)
                        {
                            *write_head = current_value + 1;
                            accepting = true;
                            write_head -= 4;
                        }
                    }
                }
                if (accepting == false)
                {
                    *write_head = current_value;
                    write_head -= 4;
                }
                while (write_head > board + column - 4)
                {
                    *write_head = 0;
                    write_head -= 4;
                }
            }
            break;
        default:
            std::cout << "INVALID DIRECTION SPECIFIED FOR move!" << std::endl;
            break;
    }
}
