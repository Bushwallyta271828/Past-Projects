from __future__ import division
from pylab import *
import threading
import Function
import Optimize
import ValueVar
import Infinity

def timed_optimizer(function, spacing, time):
	minholder = ValueVar.ValueVar(Infinity.Infinity())
	t = threading.Thread(target=Optimize.optimize, args=[function, spacing, minholder])
	t.daemon = True
	t.start()
	t.join(time)
	return minholder.x
