from __future__ import division
from pylab import *
from today import today
import os

def __main__():
    """
    This program opens the latest
    day in the raw directory.
    """
    path = today()
    os.system("vim \"" + path + "\"")

if __name__=="__main__":
    __main__()
