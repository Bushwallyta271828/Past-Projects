from __future__ import division
from pylab import *
from scipy.optimize import minimize
import threading
import os
import fun_gen
import Evaluate
import Val
import SpecificOptimize

class Solution:
	def __init__(self, points=None):
		if points == None:
			self.points = fun_gen.fun_gen()
		else:
			self.points = points

	def merge(self, other):
		new_points = []
		spoints = self.points
		opoints = other.points
		length = len(spoints)
		for pointnum, spoint in enumerate(spoints):
			opoint = opoints[pointnum]
			new_point = (pointnum / (length - 1)) * (opoint - spoint) + spoint
			new_points.append(new_point)
		new_solution  = Solution(new_points)
		return new_solution

	def optimize(self, time=None):
		if time == None:
			os.system("cp scr_backup.rkt scr.rkt")
			points = self.points
			domain = [(0, 1) for i in range(len(points))]
			maxholder = Val.Val([-1 for i in range(len(points))], 0)
			minimize(Evaluate.evaluate, points, args=([maxholder]), method="TNC", bounds=domain)
			return maxholder
		else:
			os.system("cp scr_backup.rkt scr.rkt")
			points = self.points
			maxholder = Val.Val([-1 for i in range(len(points))], 0)
			t = threading.Thread(target=SpecificOptimize.specific_optimize, args=[points, maxholder])
			t.daemon = True
			t.start()
			t.join(time)
			return maxholder
