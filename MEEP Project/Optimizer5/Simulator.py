from __future__ import division
from pylab import *
import Solution

values = {}

def iterate(solutions):
	sorted_solutions = sorted(solutions, key=lambda solution: -solution.amp())
	to_keep = sorted_solutions[:len(sorted_solutions)//2]
	new_solutions = to_keep
	length = len(to_keep)
	for i in range(len(sorted_solutions) - len(sorted_solutions)//2):
		parent1 = to_keep[int(random() * length)]
		parent2 = to_keep[int(random() * length)]
		new_child = parent1.breed(parent2)
		new_solutions.append(new_child)
		values[tuple(new_child.points)] = new_child.amp()
	for solution in solutions:
		solution.optimize()
		values[tuple(solution.points)] = solution.amp()
	return solutions

n = 20
population_size = 8
iters = 12
population = []
for i in range(population_size):
	points = [random() for i in range(n)]
	population.append(Solution.Solution(points))
for i in range(iters):
	population = iterate(population)
best = 0
best_solution = [-1]
for key in values:
	if values[key] > best:
		best = values[key]
		best_solution = key
print "\n\n\n\n\n"
print "BEST VALUE:"
print best
print "CORRESPONDING SOLUTION:"
print best_solution
