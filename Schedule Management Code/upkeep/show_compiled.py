from __future__ import division
from pylab import *
from today import today

def __main__():
    """
    This function prints the latest
    compiled day.
    """
    path = today()
    comp_path = path.replace("raw", "compiled")
    g = open(comp_path)
    lines = g.readlines()
    g.close()
    for l in lines: print l[:-1]

if __name__=="__main__":
    __main__()
