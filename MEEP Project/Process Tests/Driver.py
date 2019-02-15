from __future__ import division
from pylab import *
from Function import *
from Optimizer import *
import os

def quadratic(x):
	return (x - 1/2)**2 + 1/2

args = sys.argv
if len(args) == 1:
	n = 20
else:
	n = int(args[1])

f = Function(quadratic)
os.system("rm output.txt")
result = optimize(f, n)
print result
