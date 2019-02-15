from __future__ import division
from pylab import *
import call
from scipy.optimize import minimize

class Solution:
	def __init__(self, points):
		self.points = points

	def amp(self, res=75):
		return call.call(self.points, res)

	def breed(self, other, method="average"):
		if method == "average":
			new_points = [(i + other.points[inum])/2 for inum, i in enumerate(self.points)]
			new_solution = Solution(new_points)
			return new_solution
	
	def optimize(self):
		def optimizable(points):
			return -self.amp()
		initial_guess = self.points
		result = minimize(optimizable, initial_guess, method="TNC", bounds=[(0, 1) for i in range(len(initial_guess))])
		new_points = result.x
		self = Solution(new_points)
