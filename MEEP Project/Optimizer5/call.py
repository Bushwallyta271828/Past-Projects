from __future__ import division
from pylab import *
import os

ROOT = "/home/xander/Dropbox/Scheme"

def call(points, res=75):
	"""
	evaluates the amplification for some funnel.
	points is a list of the coordinates of the funnel. (LIST)
	res is the resolution used for the simulation (INT)
	"""
	print "res = " + str(res)
	print "points = " + str(points)
	scr = open(ROOT + "/MEEP Code/scr.rkt")
	lines = scr.readlines()
	scr.close()
	for linenum, line in enumerate(lines):
		if "(define-param points (list" in line:
			new_line = "(define-param points (list"
			for point in points:
				new_line += " " + str(point)
			new_line += ")) ;These are the coordinates of the vertices.\n"
			lines[linenum] = new_line
		if "(define-param res" in line:
			new_line = "(define-param res "
			new_line += str(res)
			new_line += ") ;This is the resolution of the grid.\n"
			lines[linenum] = new_line
	write_scr = open(ROOT + "/MEEP Code/scr.rkt", "w")
	for line in lines:
		write_scr.write(line)
	write_scr.close()
	os.system('meep "' + ROOT + '/MEEP Code/scr.rkt" > ' + ROOT + "/Optimizer5/call_output.txt")
	f = open("call_output.txt")
	lines = f.readlines()
	f.close()
	line = lines[-1][:-1]
	result = float(line)
	print "result = " + str(result)
	return result
