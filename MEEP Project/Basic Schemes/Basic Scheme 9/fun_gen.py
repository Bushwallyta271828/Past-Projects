from __future__ import division
from pylab import *

def fun_gen(n=10, deviation=0.4):
	fun = [1]
	for i in range(n - 1):
                last = fun[-1]
       	        upper_bound = (1 - last)*deviation*(n + 1 - i)/(n + 1) + last
               	lower_bound = last - last*deviation*(i + 1)/(n + 1)
                value = (upper_bound - lower_bound)*random() + lower_bound
       	        fun.append(value)
	return fun
