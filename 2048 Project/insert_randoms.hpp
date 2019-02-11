#ifndef INSERT_RANDOMS_HPP
#define INSERT_RANDOMS_HPP

#define PROB 0.1
//PROB is the probability of a 4 occuring as the random number
//after a move. PROB should be a multiple of 0.01.
//I'm putting this constant here (and not in insert_randoms.cpp)
//because other functions may use it - however, the constant
//fundamentally stems from its use in this function.

void insert_randoms(char*);

#endif // INSERT_RANDOMS_HPP
