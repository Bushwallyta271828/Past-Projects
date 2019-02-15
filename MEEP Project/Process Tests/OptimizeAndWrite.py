from __future__ import division
from pylab import *
from Optimizer import *
import os
import glob

def optimize_and_write(function, spacing):
	result = optimize(function, spacing)
	files = glob.glob("*")
	if "result.txt" in files:
		os.system("rm result.txt")
	f = open("result.txt", "w")
	f.write(str(result) + "\n")
	f.close()
	return result
