from __future__ import division
from pylab import *
from today import today

def __main__():
    """
    This function prints the latest
    raw day.
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    for l in lines: print l[:-1]

if __name__=="__main__":
    __main__()
