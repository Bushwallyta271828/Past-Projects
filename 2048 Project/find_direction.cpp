#include "find_direction.hpp"
#include "move.hpp"
#include "insert_randoms.hpp" //used for PROB variable.
#include "heuristic.hpp"
#include <chrono> //used for enforcing MAX_TIME limit.
#include <algorithm> //used for std::copy and std::equal
#include <iostream> //used for printing the depth

typedef std::chrono::steady_clock::time_point time_point;

char direction(char*, char, float*, time_point);
float expected_heuristic_time_limited(char*, char, float*, time_point);
float expected_heuristic(char*, char, float*);

char find_direction(char* board, float* coeffs)
{
    /*
     *This is the actual function
     *called by all external scripts
     *to find the optimal direction to go
     *in. It delegates the task of finding the
     *optimal direction to other functions, and
     *hence mostly just iterates over different
     *tree depths until the time limit is reached.
     *find_direction should never be passed a done board.
     *coeffs are the coefficients used in heuristic.
     */
    time_point begin = std::chrono::steady_clock::now();
    char depth = TIME_DEPTH; //the depth of the search
    char best_direction; // the direction find_direction advises to go in.
    char claimed_direction; //best_direction will be set to this so long as claimed_direction is not -1, in which case best_direction will be returned.
    //First, some code will be run to pick a direction without any
    //consideration of the heuristic. This is in case all calls
    //to direction with nonzero depth take longer than the time limit - something
    //that seems highly improbable but is conceivable for large TIME_DEPTH.
    best_direction = direction(board, 0, coeffs, begin);
    if (best_direction == -1)
    {
        return best_direction;
        std::cout << "depth = 0" << std::endl;
        //find_direction should never be passed
        //a done board, and best_direction will only
        //continue to be -1 if this is the case.
    }
    while (true)
    {
        claimed_direction = direction(board, depth, coeffs, begin);
        if (claimed_direction == -1)
        {
            std::cout << "depth = " << (depth - 1) << std::endl;
            return best_direction;
        }
        else
        {
            best_direction = claimed_direction;
        }
        depth++;
    }
}

char direction(char* board, char d, float* coeffs, time_point beginning)
{
    /*
     *direction is the function called directly
     *by find_direction to find the optimal direction
     *to travel in at a particualr tree depth.
     *Although upon calling depth should be
     *greater than or equal to TIME_DEPTH or equal to 0,
     *a clause exists to work correctly even if
     *this is not the case.
     *If the function returns -1, then the
     *time limit has been reached.
     *coeffs is used in heuristic.
     */
    if (d == 0)
    {
        char best_direction = -1;
        char testing_direction = 0;
        bool same;
        char new_board[16];
        std::copy(board, board + 16, new_board);
        while ((best_direction == -1) && (testing_direction < 4))
        {
            move_no_score(new_board, testing_direction);
            same = std::equal(board, board + 16, new_board);
            if (!same)
            {
                best_direction = testing_direction;
            }
            testing_direction++;
        }
        return best_direction;
    }
    else if (d < TIME_DEPTH)
    {
        //This clause should never fire.
        char new_board[16];
        float average_increase;
        float best_average_increase = 0;
        char best_direction = -1;
        char counter;
        bool same;
        for (char direction = 0; direction < 4; ++direction)
        {
            std::copy(board, board + 16, new_board);
            move_no_score(new_board, direction);
            same = std::equal(board, board + 16, new_board);
            if (!same)
            {
                average_increase = 0;
                counter = 0;
                for (int pos = 0; pos < 16; ++pos)
                {
                    if (new_board[pos] == 0)
                    {
                        counter++;
                        new_board[pos] = 1;
                        float improvement_2 = expected_heuristic(new_board, d - 1, coeffs);
                        new_board[pos] = 2;
                        float improvement_4 = expected_heuristic(new_board, d - 1, coeffs);
                        average_increase += (1 - PROB) * improvement_2 + PROB * improvement_4;
                    }
                }
                average_increase /= counter;
                if (average_increase > best_average_increase)
                {
                    best_average_increase = average_increase;
                    best_direction = direction;
                }
            }
        }
        return best_direction;
    }
    else //d >= TIME_DEPTH
    {
        char new_board[16];
        float average_increase;
        float best_average_increase = 0;
        char best_direction = -1;
        char counter;
        bool same;
        for (char direction = 0; direction < 4; ++direction)
        {
            std::copy(board, board + 16, new_board);
            move_no_score(new_board, direction);
            same = std::equal(board, board + 16, new_board);
            if (!same)
            {
                average_increase = 0;
                counter = 0;
                for (int pos = 0; pos < 16; ++pos)
                {
                    if (new_board[pos] == 0)
                    {
                        counter++;
                        new_board[pos] = 1;
                        float improvement_2 = expected_heuristic_time_limited(new_board, d - 1, coeffs, beginning);
                        if (improvement_2 == -1)
                        {
                            return -1;
                        }
                        new_board[pos] = 2;
                        float improvement_4 = expected_heuristic_time_limited(new_board, d - 1, coeffs, beginning);
                        if (improvement_4 == -1)
                        {
                            return -1;
                        }
                        average_increase += (1 - PROB) * improvement_2 + PROB * improvement_4;
                    }
                }
                average_increase /= counter;
                if (average_increase > best_average_increase)
                {
                    best_average_increase = average_increase;
                    best_direction = direction;
                }
            }
        }
        return best_direction;
    }
}

float expected_heuristic_time_limited(char* board, char d, float* coeffs, time_point beginning)
{
    /*
     *expected_heuristic_time_limited is the function almost always
     *called by direction. expected_heuristic_time_limited is just
     *like expected_heuristic, only expected_heuristic_time_limited checks
     *up on the time and also handles correctly recursive calls that throw
     *-1 returns (i.e. time is up).
     *coeffs is used for heuristic.
     */
    time_point now = std::chrono::steady_clock::now();
    long long int duration = (long long int)(std::chrono::duration_cast<std::chrono::nanoseconds>(now - beginning).count());
    if (duration > (long long int)(((long long int) (MAX_TIME * 10000)) * 100000)) //the billion is to convert from seconds to nanoseconds
    {
        return -1;
    }
    if (d == 0)
    {
        return heuristic(board, coeffs);
    }
    else
    {
        char new_board[16];
        float average_increase;
        float best_average_increase = 0;
        char counter;
        bool same;
        for (char direction = 0; direction < 4; ++direction)
        {
            std::copy(board, board + 16, new_board);
            move_no_score(new_board, direction);
            same = std::equal(board, board + 16, new_board);
            if (!same)
            {
                average_increase = 0;
                counter = 0;
                if (d >= TIME_DEPTH)
                {
                    for (int pos = 0; pos < 16; ++pos)
                    {
                        if (new_board[pos] == 0)
                        {
                            counter++;
                            new_board[pos] = 1;
                            float improvement_2 = expected_heuristic_time_limited(new_board, d - 1, coeffs, beginning);
                            if (improvement_2 == -1)
                            {
                                return -1;
                            }
                            new_board[pos] = 2;
                            float improvement_4 = expected_heuristic_time_limited(new_board, d - 1, coeffs, beginning);
                            if (improvement_4 == -1)
                            {
                                return -1;
                            }
                            average_increase += (1 - PROB) * improvement_2 + PROB * improvement_4;
                        }
                    }
                }
                else //d = TIME_DEPTH - 1
                {
                    for (int pos = 0; pos < 16; ++pos)
                    {
                        if (new_board[pos] == 0)
                        {
                            counter++;
                            new_board[pos] = 1;
                            float improvement_2 = expected_heuristic(new_board, d - 1, coeffs);
                            new_board[pos] = 2;
                            float improvement_4 = expected_heuristic(new_board, d - 1, coeffs);
                            average_increase += (1 - PROB) * improvement_2 + PROB * improvement_4;
                        }
                    }
                }
                average_increase /= counter;
                if (average_increase > best_average_increase)
                {
                    best_average_increase = average_increase;
                }
            }
        }
        return best_average_increase;
    }
}

float expected_heuristic(char* board, char d, float* coeffs)
{
    /*
     *expected_heuristic calculates
     *the expectation value of the heuristic
     *d moves in the future. time limits are not considered.
     *coeffs is used for heuristic.
     */
    if (d == 0)
    {
        return heuristic(board, coeffs);
    }
    else
    {
        char new_board[16];
        float average_increase;
        float best_average_increase = 0;
        char counter;
        bool same;
        for (char direction = 0; direction < 4; ++direction)
        {
            std::copy(board, board + 16, new_board);
            move_no_score(new_board, direction);
            same = std::equal(board, board + 16, new_board);
            if (!same)
            {
                average_increase = 0;
                counter = 0;
                for (int pos = 0; pos < 16; ++pos)
                {
                    if (new_board[pos] == 0)
                    {
                        counter++;
                        new_board[pos] = 1;
                        float improvement_2 = expected_heuristic(new_board, d - 1, coeffs);
                        new_board[pos] = 2;
                        float improvement_4 = expected_heuristic(new_board, d - 1, coeffs);
                        average_increase += (1 - PROB) * improvement_2 + PROB * improvement_4;
                    }
                }
                average_increase /= counter;
                if (average_increase > best_average_increase)
                {
                    best_average_increase = average_increase;
                }
            }
        }
        return best_average_increase;
    }
}
