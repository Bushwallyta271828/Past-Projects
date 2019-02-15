from __future__ import division
from pylab import *
import ValueVar

class Function:
	def __init__(self, f):
		self.f = f

	def __call__(self, x, minholder):
		f = self.f
		value = f(x)
		if value < minholder.x:
			minholder.x = value
		return value
