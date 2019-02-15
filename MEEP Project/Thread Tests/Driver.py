from __future__ import division
from pylab import *
import TimedOptimizer
import Function

def f(x):
	return (x - 0.5)**2 + 0.5

args = sys.argv
if len(args) == 1:
	spacing = 1000
else:
	string_spacing = args[1]
	spacing = int(string_spacing)
function = Function.Function(f)
value = TimedOptimizer.timed_optimizer(function, spacing, 1)
print value
