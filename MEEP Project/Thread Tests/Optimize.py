from __future__ import division
from pylab import *
import Function

def optimize(function, spacing, minholder):
	values = []
	for i in range(spacing + 1):
		x = i / spacing
		value = function(x, minholder)
		values.append(value)
	return min(values)
