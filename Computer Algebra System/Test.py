from __future__ import division
from pylab import *
from sympy import *
from Junction import *
from Leaf import *

root = Junction()
child1 = Leaf(3)
child2 = Leaf(5)
root.set_node("+", [child1, child2])
print root.evaluate()
