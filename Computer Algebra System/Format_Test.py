from __future__ import division
from pylab import *
from sympy import *
import Format
import Leaf_format

#Format:
#          ()
#         /  \
#        /    \
#       /      \
#      ()       ()
#     /  \
#    /    \
#   /      \
#  ()       ()


LA = Leaf_format.Leaf_format()
LB = Leaf_format.Leaf_format()
LC = Leaf_format.Leaf_format()
LJ = Format.Format([LA, LB])
TJ = Format.Format([LJ, LC])
e, x, pi = symbols("e x pi", real=True)
values = TJ.values(e, pi, x)
for value in values:
	print value.evaluate()
