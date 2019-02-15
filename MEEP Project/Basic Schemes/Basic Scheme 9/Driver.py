from __future__ import division
from pylab import *
import os
import Solution

s = Solution.Solution()
result = s.optimize(10*60)
print result.x
print result.pointx
print "\n"*25
os.system("rm *.pyc")
