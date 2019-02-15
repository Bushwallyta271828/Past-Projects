from __future__ import division
from pylab import *
from day_compile import *
import sys
import glob
from day_number import day_number

def comp_range():
    """
    This function compiles all
    days from the first command-line
    argument to and including the second command-line
    argument in "raw", and writes the compiled
    files in "compiled".
    """
    start_day = sys.argv[1]
    stop_day = sys.argv[2]
    file_paths = glob.glob("../times/raw/*")
    names = [file_path.split("/")[-1] for file_path in file_paths]
    names.sort(key=lambda name:day_number(name))
    start_index = names.index(start_day)
    stop_index = names.index(stop_day) + 1
    for name in names[start_index: stop_index]:
        comp("../times/raw/" + name, "../times/compiled/" + name)

if __name__=="__main__":
    comp_range()

