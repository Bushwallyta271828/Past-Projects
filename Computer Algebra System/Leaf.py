from __future__ import division
from pylab import *
from sympy import *

class Leaf:
	def __init__(self, value=None):
		self.value = value

	def set_value(self, value):
		self.value = value

	def replace(self, element, new_value):
		value = self.value
		if value == element:
			self.value = new_value

	def evaluate(self):
		return self.value
