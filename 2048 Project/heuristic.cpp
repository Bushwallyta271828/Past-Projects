#include "heuristic.hpp"
#include <numeric> //used for std::accumulate
#include <algorithm> //used for std::count

inline float H1(char* board);
inline float H2(char* board);
inline float H3(char* board);
inline float H4(char* board);

float heuristic(char* board, float* coeffs)
{
    /*
     *This is the function find_direction
      seeks to optimize. 
     *It must always return a positive number.
     */
    float h1 = H1(board);
    float h2 = H2(board);
    float h3 = H3(board);
    float h4 = H4(board);
    return coeffs[0] * h1
         + coeffs[1] * h2
         + coeffs[2] * h3
         + coeffs[3] * h4;
}

inline float H1(char* board)
{
    /*
     *This function returns 
      the sum of the elements of the board.
     */
    float total = 0;
    for (int i = 0; i < 16; ++i)
    {
        total += (1 << board[i]);
    }
    return total;
}

inline float H2(char* board)
{
    /*
     *This function returns the number
      of zeroes the board possesses. 
     */
    return (float) std::count(board, board + 16, 0);
}

inline float H3(char* board)
{
    /*
     *coming back
     */
    int value;
    int new_value;
    float counter = 0;
    for (int i = 0; i < 16; ++i)
    {
        value = board[i];
        if ((i % 4) > 0)
        {
            new_value = board[i - 1];
            if ((new_value == value) || (new_value == value - 1))
            {
                counter += (1 << value);
            }
        }
        if ((i % 4) < 3)
        {
            new_value = board[i + 1];
            if ((new_value == value) || (new_value == value - 1))
            {
                counter += (1 << value);
            }
        }
        if (i > 3)
        {
            new_value = board[i - 4];
            if ((new_value == value) || (new_value == value - 1))
            {
                counter += (1 << value);
            }
        }
        if (i < 12)
        {
            new_value = board[i + 4];
            if ((new_value == value) || (new_value == value - 1))
            {
                counter += (1 << value);
            }
        }
    }
    return counter;
}

inline float H4(char* board)
{
    /*
     *coming back
     */
    return (float) std::accumulate(board, board + 16, 0);
}
