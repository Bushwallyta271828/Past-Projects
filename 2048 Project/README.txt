Thoughts:

Use omp and eventually cuda (which would involve setting up a makefile that behaves with cuda) to dramatically speed up computations.
Really tinker with heuristic.cpp so that, instead of calling an arbitrary function I make, I either evolve over the coefficients or write a neural network to do something. Most of the future gain in performance will likely be due to improving heuristic.cpp, not find_direction.cpp itself.
