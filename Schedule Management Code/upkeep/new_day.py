from __future__ import division
from pylab import *
import sys
from datetime import datetime

def __main__():
    """
    This function creates 
    a new, empty file, representing
    today.
    """
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    day_to_string = [None  ,
                     "1st" ,
                     "2nd" ,
                     "3rd" ,
                     "4th" ,
                     "5th" ,
                     "6th" ,
                     "7th" ,
                     "8th" ,
                     "9th" ,
                     "10th",
                     "11th",
                     "12th",
                     "13th",
                     "14th",
                     "15th",
                     "16th",
                     "17th",
                     "18th",
                     "19th",
                     "20th",
                     "21st",
                     "22nd",
                     "23rd",
                     "24th",
                     "25th",
                     "26th",
                     "27th",
                     "28th",
                     "29th",
                     "30th",
                     "31st"]
    day_string = day_to_string[day]
    month_to_string = [None       ,
                       "January"  ,
                       "February" ,
                       "March"    ,
                       "April"    ,
                       "May"      ,
                       "June"     ,
                       "July"     ,
                       "August"   ,
                       "September",
                       "October"  ,
                       "November" ,
                       "December" ]
    month_string = month_to_string[month]
    year_string = str(year)
    name = day_string + " " + month_string + " - " + year_string
    print name
    file_path = "../times/raw/" + name
    open(file_path, "a").close()

if __name__=="__main__":
    __main__()
