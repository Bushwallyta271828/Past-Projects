from __future__ import division
from pylab import *

def is_time(string):
    """
    This function determines
    whether the provided string is
    an understandable duration of
    time.
    For instance:
    * 1 minute
    * 10 minutes
    * 1 hour
    * 5 hours 37 minutes
    are all valid times (would return True), while
    * 0 minutes
    * 1 minutes
    * 5 minute
    * 1 hours
    * 5 minutes 7 hours
    * 7 hours 50 minutes 30 minutes
    are all invalid (would return False).
    Used by valid syntax checker.
    """
    spl = string.split()
    if len(spl) == 0: return False
    for i in spl:
        if not ((i.isdigit() and
                 int(i) > 0 and
                 int(i) < 60) or
                (i in ["minute",
                       "minutes",
                       "hour",
                       "hours"])):
            return False
    for inum, i in enumerate(spl):
        if i.isdigit():
            if (len(spl) == inum - 1 or
                spl[inum + 1].isdigit()):
                return False
            if (i == "1" and
                (spl[inum + 1] in ["hours", "minutes"])):
                return False
            if (i != "1" and
                (spl[inum + 1] in ["hour", "minute"])):
                return False
    if spl.count("hour") + spl.count("hours") > 1:
        return False
    if spl.count("minute") + spl.count("minutes") > 1:
        return False
    if (("hour" in spl or "hours" in spl) and
        ("minute" in spl or "minutes" in spl)):
        if string.index("hour") > string.index("minute"):
            return False
    return True

def is_stamp(string):
    """
    This function determines whether
    a string is a valid time STAMP, i.e.
    of the form HH:MM on a 24-hour clock
    """
    if string.count(":") != 1: return False
    hours = string[:string.index(":")]
    minutes = string[string.index(":") + 1:]
    if not hours.isdigit(): return False
    if not minutes.isdigit(): return False
    if int(hours) > 23: return False
    if int(minutes) > 59: return False
    return True
