from __future__ import division
from pylab import *
import glob

def today():
    """
    This function returns the path
    to the latest day.
    """
    file_paths = glob.glob("../times/raw/*")
    names = [file_path.split("/")[-1] for file_path in file_paths]
    month_options = ["January",
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
    days = [int(name.split(" ")[0][:-2]) for name in names]
    months = [month_options.index(name.split(" ")[1]) for name in names]
    years = [int(name.split(" ")[-1]) for name in names]
    latest_index = -1
    latest_year = 0
    latest_month = -1
    latest_day = 0
    for i in range(len(names)):
        if years[i] > latest_year:
            latest_index = i
            latest_year = years[i]
            latest_month = months[i]
            latest_day = days[i]
        elif years[i] == latest_year:
            if months[i] > latest_month:
                latest_index = i
                latest_month = months[i]
                latest_day = days[i]
            elif months[i] == latest_month:
                if days[i] > latest_day:
                    latest_index = i
                    latest_day = days[i]
    return "../times/raw/" + names[latest_index]
