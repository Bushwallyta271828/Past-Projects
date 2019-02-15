from __future__ import division
from pylab import *
from OptimizeAndWrite import *
from Function import *
import thread
import time
import glob
import os

def timed_optimizer(function, spacing, time_limit):
	try:
		thread.start_new_thread(optimize_and_write, (function, spacing))
		time.sleep(time_limit)
		files = glob.glob("*")
		if "result.txt" in files:
			f = open("result.txt")
			lines = f.readlines()
			f.close()
			real_line = lines[0][:-1]
			value = float(real_line)
			
	except:
		print "Error: unable to create new Thread."
