from __future__ import division
from pylab import *
from today import today
import sys

def __main__():
    """
    This function appends the one 
    keyword argument to the latest raw
    file.
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    line = sys.argv[1] + "\n"
    for l in lines + [line]: print l[:-1]
    f = open(path, "a")
    f.write(line)
    f.close()

if __name__=="__main__":
    __main__()
