from __future__ import division
from pylab import *
import sys
import glob
from day_number import day_number

def __main__():
    """
    This is the function that gets called
    when the program is run. It produces a  
    "slice" of one of the old files from a given
    start to a given stop date. The third optional
    command-line argument specifies whether the desired slice
    is of the raw data or the compiled data. (Say "raw" for raw
    and "compiled" for compiled)
    If only one command-line argument is given, it reads that 
    as the form ("raw" or "compiled"), and produces the corresponding
    file for all days.
    """
    if len(sys.argv) == 4:
        start_day = sys.argv[1]
        stop_day = sys.argv[2]
        form = sys.argv[3]
    elif len(sys.argv) == 2:
        form = sys.argv[1]
    file_paths = glob.glob("../times/" + form + "/*")
    names = [file_path.split("/")[-1] for file_path in file_paths]
    names.sort(key=lambda name: day_number(name))
    if len(sys.argv) == 4:
        names = names[names.index(start_day): names.index(stop_day) + 1]
    file_paths = ["../times/" + form + "/" + name for name in names]
    slice_lines = []
    for file_path_num, file_path in enumerate(file_paths):
        f = open(file_path)
        lines = f.readlines()
        f.close()
        slice_lines.append(names[file_path_num] + "\n")
        slice_lines.append("\n")
        slice_lines += lines
        slice_lines += ["\n", "\n"]
    slice_lines = slice_lines[:-2]
    output = open("slice_file.txt", "w")
    for slice_line in slice_lines:
        output.write(slice_line)
    output.close()

if __name__=="__main__":
    __main__()
