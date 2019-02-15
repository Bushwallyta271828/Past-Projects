from __future__ import division
from day_compile import *
import glob

def comp_all():
    """
    This function compiles every day in raw
    to the appropriate file in compiled.
    """
    names = glob.glob("../times/raw/*")
    file_names = [name.split("/")[-1] for name in names]
    comp_names = ["../times/compiled/" + file_name for file_name in file_names]
    for i in range(len(names)):
        comp(names[i], comp_names[i])

if __name__=="__main__":
    comp_all()
