from __future__ import division
from pylab import *
from today import today
import sys

def __main__():
    """
    This function subtracts the given
    an amount of work from the
    most recent day. The amount of time
    to take off is passed in the format:
        python subtract.py hours minutes
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    hours = int(sys.argv[1])
    minutes = int(sys.argv[2])
    line = " - "
    if hours == 1: line += "1 hour "
    elif hours > 1: line += str(hours) + " hours "
    if minutes == 1: line += "1 minute"
    elif minutes > 1: line += str(minutes) + " minutes"
    line += "\n"
    for l in lines + [line]: print l[:-1]
    f = open(path, "a")
    f.write(line)
    f.close()

if __name__=="__main__":
    __main__()
