#ifndef FIND_DIRECTION_HPP
#define FIND_DIRECTION_HPP

#define MAX_TIME 0.1
//This is the maximum amount of time the find_direction queries are allowed to take.
//This must be a multiple of 0.0001.

#define TIME_DEPTH 3
//This is the depth at and above which the time since the first function call is evaluated.
//If too low, the continued checks might slow down the program. If too high, the program might not know soon enough when it has reached the time limit.
//find_direction starts checking depths at TIME_DEPTH and continues upward.

char find_direction(char*, float*);

#endif // FIND_DIRECTION_HPP
