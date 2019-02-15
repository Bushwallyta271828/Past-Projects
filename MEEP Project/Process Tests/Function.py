from __future__ import division
from pylab import *

class Function:
	def __init__(self, f):
		self.f = f

	def evaluate(self, x):
		f = self.f
		value = f(x)
		output = open("output.txt", "a")
		output.write(str(x) + " : " + str(value) + "\n")
		output.close()
		return value
