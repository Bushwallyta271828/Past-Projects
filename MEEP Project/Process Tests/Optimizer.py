from __future__ import division
from pylab import *

#DO
#NOT
#GO
#NEAR
#THIS
#CODE
#WITH
#A
#TEN
#FOOT
#POLE!!!
def optimize(function, spacing):
	values = []
	for i in range(spacing + 1):
		x = i / spacing
		value = function.evaluate(x)
		values.append(value)
	return min(values)
