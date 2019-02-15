from __future__ import division
from pylab import *
from sympy import *
import Leaf

class Leaf_format:
	def __init__(self):
		pass

	def values(self, e, pi, x):
		E = Leaf.Leaf(e)
		PI = Leaf.Leaf(pi)
		X = Leaf.Leaf(x)
		return [E, PI, X]
