from __future__ import division
from pylab import *
from today import today
import sys
from datetime import datetime

def __main__():
    """
    This function puts a "stop"
    clause in the latest raw file.
    """
    path = today()
    g = open(path)
    lines_original = g.readlines()
    g.close()
    lines = [" ".join([word for word in line.split(" ") if word]) for line in lines_original if line[:-1]]
    last_index = len(lines) - 1
    while lines[last_index][0] in ["-", "<", "#", "%", "."]: last_index -= 1
    last_line = lines[last_index]
    subject = last_line[6:last_line.index(" @ ")]
    now = datetime.time(datetime.now())
    now_string = ("0"*(2 - len(str(now.hour))) + str(now.hour)
                + ":" + "0"*(2 - len(str(now.minute))) + str(now.minute))
    line = "stop " + subject + " @ " + now_string + "\n"
    for l in lines_original + [line,]: print l[:-1]
    f = open(path, "a")
    f.write(line)
    f.close()

if __name__=="__main__":
    __main__()
