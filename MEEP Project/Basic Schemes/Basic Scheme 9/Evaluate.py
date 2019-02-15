from __future__ import division
from pylab import *
import call
import acceptable

def evaluate(points, *args):
	maxholder = args[0]
	value = call.call(points)
	if value > maxholder.get_x():
		if acceptable.acceptable(points):
			maxholder.set_x(value)
			maxholder.set_points(points)
	return value
