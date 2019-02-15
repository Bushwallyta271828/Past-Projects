from __future__ import division
from pylab import *

class Val:
	def __init__(self, points, x):
		self.points = points
		self.x = x

	def set_x(self, x):
		self.x = x

	def set_points(self, points):
		self.points = points

	def get_x(self):
		return self.x

	def get_points(self):
		return self.points

	def __str__(self):
		x = self.x
		points = self.points
		String = "Val("
		String += "x = " + str(x)
		String += ", points = " + str(points)
		String += ")"
		return String
