from __future__ import division
from pylab import *
from today import today
import sys

def __main__():
    """
    This function adds the given
    an amount of work to the
    most recent day of the given subject.
    The amount of time to add is passed in the format:
        python add.py subject hours minutes
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    subject = sys.argv[1]
    hours = int(sys.argv[2])
    minutes = int(sys.argv[3])
    line = " + "
    if hours == 1: line += "1 hour "
    elif hours > 1: line += str(hours) + " hours "
    if minutes == 1: line += "1 minute "
    elif minutes > 1: line += str(minutes) + " minutes "
    line += subject + "\n"
    for l in lines + [line]: print l[:-1]
    f = open(path, "a")
    f.write(line)
    f.close()

if __name__=="__main__":
    __main__()
