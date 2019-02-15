from __future__ import division
from pylab import *
from day_check import day_check
from date_check import date_check
from day_number import day_number
import glob

def checker():
    """
    This function is the master error-checking function.
    It appropriately delegates the error checking to date_check
    and day_check, which examine the times log for faulty date titles
    and faulty file contents, respectively. It places the output of
    date_check in Times/checking/date_check_output.txt, while it places
    the output of day_check in Times/times/check_files/*, where the *
    is the same file name as the raw file possessed (i.e. the date).
    It also saves and prints all of these error messages together in checker_output.txt.
    It does not check the current day (there may likely be an open clause etc.)
    No checking of the compiled files is performed (they are computed
    automatically, not written manually).
    """
    report = ""
    date_check("date_check_output.txt")
    f = open("date_check_output.txt")
    lines = f.readlines()
    f.close()
    errors = [line.replace(" ","").replace("\n","") != "" for line in lines]
    if sum(errors) > 0:
        report += ''.join(lines)
        report += "\n\n"
    long_file_names = glob.glob("../times/raw/*")
    short_file_names = [long_file_name.split("/")[-1] for long_file_name in long_file_names]
    short_file_names.sort(key = lambda name: day_number(name))
    short_file_names = short_file_names[:-1] #the current day shouldn't be checked.
    for short_file_name in short_file_names:
        day_check("../times/raw/" + short_file_name, "../times/check_files/" + short_file_name)
        g = open("../times/check_files/" + short_file_name)
        lines = g.readlines()
        g.close()
        errors = [line.replace(" ","").replace("\n","") != "" for line in lines]
        if sum(errors) > 0:
            report += short_file_name + ":\n"
            report += ''.join(lines)
            report += "\n\n"
    print report
    h = open("checker_output.txt", "w")
    h.write(report)
    h.close()

if __name__=="__main__":
    checker()
