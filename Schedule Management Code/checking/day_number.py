from __future__ import division
from pylab import *

def day_number(name):
    """
    This function returns the 
    key function for sorting
    a list of dates.
    """
    day = int(name.split(" ")[0][:-2])
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]
    month = months.index(name.split(" ")[1])
    year = int(name.split(" ")[-1])
    return day + 50*month + 1000*year
