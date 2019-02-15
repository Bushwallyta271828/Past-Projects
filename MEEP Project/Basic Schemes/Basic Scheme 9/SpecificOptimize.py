from __future__ import division
from pylab import *
from scipy.optimize import minimize
import Evaluate

def specific_optimize(points, maxholder):
	function = Evaluate.evaluate
	x0 = points
	args = ([maxholder])
	method = "TNC"
	bounds = [(0, 1) for i in range(len(points))]
	minimize(function, x0, args=args, method=method, bounds=bounds)
