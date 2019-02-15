from __future__ import division
from pylab import *
from sympy import *
from Junction import *
from Leaf import *

x, e, pi = symbols("x e pi", real=True)

def upgrade_leaf(leaf):
	value = leaf.value
	if value == pi:
		new_leaf = Leaf.Leaf(e)
		return new_leaf
	elif value == e:
		new_leaf = Leaf.Leaf(x)
		return new_leaf
	elif value == x:
		new_junction = Junction.Junction()
		

def generate(n):
	"""
	n is the number of equations to generate
	"""
	
