from __future__ import division
from pylab import *

def acceptable(points):
	result = True
	for point in points:
		if point < 0 or point > 1:
			result = False
	return result
