from __future__ import division
from pylab import *
import Junction
import Leaf_format
import Leaf

class Format:
	def __init__(self, children=None): self.children = children

	def set_children(self, children): self.children = children

	def values(self, e, pi, x):
		children = self.children
		solutions = []
		if len(children) == 1:
			available = ["sin", "log"]
			child_solutions = child.values(e, pi, x)
			for child_solution in child_solutions:
				for attribute in available:
					solutions.append(Junction.Junction(attribute, [child_solution]))
			return solutions
		elif len(children) == 2:
			available = ["+", "*", "**"]
			left_child, right_child = children
			left_child_solutions = left_child.values(e, pi, x)
			right_child_solutions = right_child.values(e, pi, x)
			for left_child_solution in left_child_solutions:
				for right_child_solution in right_child_solutions:
					for attribute in available:
						solution = Junction.Junction(attribute, [left_child_solution, right_child_solution])
						solutions.append(solution)
			return solutions
