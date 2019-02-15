from __future__ import division
from pylab import *
import sys
import glob
from day_number import day_number
import re

def __main__():
    """
    This function replaces the first keyword
    argument subject with the second keyword
    argument subject. The optional start and
    stop date arguments are self-explanatory.
    """
    former = sys.argv[1]
    latter = sys.argv[2]
    former = " ".join(former.split())
    latter = " ".join(latter.split())
    file_paths = glob.glob("../times/raw/*")
    if len(sys.argv) == 5: #Do part-data work...
        names = [file_path.split("/")[-1] for file_path in file_paths]
        start = sys.argv[3]
        stop = sys.argv[4]
        names.sort(key=lambda name: day_number(name))
        names = names[names.index(start): names.index(stop) + 1]
        file_paths = ["../times/raw/" + name for name in names]
    for file_path in file_paths:
        f = open(file_path)
        lines = f.readlines()
        f.close()
        newlines = []
        for line in lines:
            line = " ".join(line.split())
            defined = False
            m = re.match("start " + former + " @ (\d+):(\d+)", line)
            if m:
                hour, minute = m.groups()
                nline = " ".join(("start " + latter + " @ " + hour + ":" + minute).split()) + "\n"
                defined = True
            m = re.match("stop " + former + " @ (\d+):(\d+)", line)
            if m:
                hour, minute = m.groups()
                nline = " ".join(("stop " + latter + " @ " + hour + ":" + minute).split()) + "\n"
                defined = True
            cline = line.split(" ")
            if len(cline) > 0:
                if cline[0] == "+":
                    i = 1
                    while ((cline[i] in ["minute", "minutes", "hour", "hours"] and cline[i - 1].isdigit() == True)
                        or (cline[i].isdigit() == True and cline[i + 1] in ["minute", "minutes", "hour", "hours"])):
                        i = i + 1
                    subject = " ".join(cline[i:])
                    if subject == former:
                        nline = line.replace(former, latter) + "\n"
                        defined = True
            if not defined: nline = line + "\n"
            newlines.append(nline)
        g = open(file_path, "w")
        for nline in newlines:
            g.write(nline)
        g.close()


if __name__=="__main__":
    __main__()
