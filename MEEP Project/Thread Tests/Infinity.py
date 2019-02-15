from __future__ import division
from pylab import *

class Infinity:
	def __init__(self):
		pass

	def __gt__(self, other):
		return True
