from __future__ import division
from pylab import *
from today import today

def __main__():
    """
    This function deletes the latest line
    in the most recent day in ../times/raw.
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    lines = lines[:-1]
    for l in lines: print l[:-1]
    f = open(path, "w")
    for l in lines: f.write(l)
    f.close()

if __name__=="__main__":
    __main__()
