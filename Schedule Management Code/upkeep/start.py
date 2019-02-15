from __future__ import division
from pylab import *
from today import today
import sys
from datetime import datetime

def __main__():
    """
    This function puts a "start"
    clause in the latest raw file.
    The one command-line argument
    specifies what subject to start.
    """
    path = today()
    g = open(path)
    lines = g.readlines()
    g.close()
    subject = sys.argv[1]
    now = datetime.time(datetime.now())
    now_string = ("0"*(2 - len(str(now.hour))) + str(now.hour)
                + ":" + "0"*(2 - len(str(now.minute))) + str(now.minute))
    line = "start " + subject + " @ " + now_string + "\n"
    for l in lines + [line]: print l[:-1]
    f = open(path, "a")
    f.write(line)
    f.close()

if __name__=="__main__":
    __main__()
