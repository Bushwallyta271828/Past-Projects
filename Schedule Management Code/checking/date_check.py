from __future__ import division
from pylab import *
from day_number import day_number
import glob

def valid_date(day, month, year):
    """
    This function performs much of the grunt-work
    of date_check. Given the day (integer), month (string),
    and year (integer), it confirms whether that
    date existed. It is both used to determine whether
    a file name is valid and used to determine whether
    a day is missing in between two other days.
    A return of 0 means that nothing is wrong
    A return of 1 means that the month is not a recognized month name
    A return of 2 means that all elements of the name are recognized, but the date didn't exist.
    """
    month_day_mapping = {"January":31,
                         "February":28, #corrects if leap year
                         "March":31,
                         "April":30,
                         "May":31,
                         "June":30,
                         "July":31,
                         "August":31,
                         "September":30,
                         "October":31,
                         "November":30,
                         "December":31}
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        month_day_mapping["February"] = 29
    if not month in month_day_mapping:
        return 1
    else:
        if day > month_day_mapping[month] or day < 1:
            return 2
        else:
            return 0

def construct_date(day, month, year):
    """
    This function properly constructs
    the date tag for a given day, month, and year.
    No checking is performed to ensure that the given
    day, month, and year are correct.
    """
    ending = "th"
    if day < 10 or day > 20:
        if day % 10 == 1: ending = "st"
        elif day % 10 == 2: ending = "nd"
        elif day % 10 == 3: ending = "rd"
    construction = str(day) + ending + " " + month + " - " + str(year)
    return construction

def date_check(out_path):
    """
    This function examines the integrity of the set
    of file names provided in the Times/times/raw/ directory.
    It looks for the two following mistakes:
        a date that is missing.
        a file that is not named with the date
    """
    long_file_names = glob.glob("../times/raw/*")
    short_file_names = [long_file_name.split("/")[-1] for long_file_name in long_file_names]
    report = ""
    for short_file_name in short_file_names:
        if "  " in short_file_name:
            report += "file \"" + short_file_name + "\": two consecutive spaces\n"
        spl = short_file_name.split()
        if spl.count("-") != 1:
            report += "file \"" + short_file_name + "\": wrong number of dashes\n"
        else:
            if spl.index("-") < len(spl) - 2:
                report += "file \"" + short_file_name + "\": more than just year trailing dash\n"
            elif spl.index("-") > len(spl) - 2:
                report += "file \"" + short_file_name + "\": year not trailing dash\n"
            else:
                if not spl[-1].isdigit():
                    report += "file \"" + short_file_name + "\": invalid year trailing dash\n"
                else:
                    year = int(spl[-1])
                    if spl.index("-") != 2:
                        report += "file \"" + short_file_name + "\": incorrect number of words (2) before dash\n"
                    else:
                        month = spl[1]
                        day_str = spl[0]
                        end_int = 0
                        while end_int < len(day_str) and day_str[end_int].isdigit():
                            end_int += 1
                        if end_int == len(day_str):
                            report += "file \"" + short_file_name + "\": no st / nd / rd / th following day number\n"
                        elif end_int == 0:
                            report += "file \"" + short_file_name + "\": no day number shown\n"
                        else:
                            day = int(day_str[0:end_int])
                            ending = "th"
                            if day < 10 or day > 20:
                                if day % 10 == 1: ending = "st"
                                elif day % 10 == 2: ending = "nd"
                                elif day % 10 == 3: ending = "rd"
                            shown_ending = day_str[end_int:]
                            if shown_ending != ending:
                                report += "file \"" + short_file_name + "\": incorrect ending after day number\n"
                            valid_date_report = valid_date(day, month, year)
                            if valid_date_report == 1:
                                report += "file \"" + short_file_name + "\": invalid month name given\n"
                            elif valid_date_report == 2:
                                report += "file \"" + short_file_name + "\": given date didn't exist\n"
    if report == "": #the rest of the code assumes that there are no errors in the syntax of the names given.
        short_file_names.sort(key=lambda name: day_number(name))
        for short_file_name_num, short_file_name in enumerate(short_file_names[:-1]):
            day = int(short_file_name.split()[0][:-2])
            month = short_file_name.split()[1]
            year = int(short_file_name.split()[-1])
            months = ["January", "February", "March",
                      "April", "May", "June",
                      "July", "August", "September",
                      "October", "November", "December"]
            missing_date = False
            if valid_date(day + 1, month, year) == 0:
                if construct_date(day + 1, month, year) != short_file_names[short_file_name_num + 1]:
                    missing_date = True
            elif month != "December":
                if construct_date(1, months[months.index(month) + 1], year) != short_file_names[short_file_name_num + 1]:
                    missing_date = True
            else:
                if construct_date(1, "January", year + 1) != short_file_names[short_file_name_num + 1]:
                    missing_date = True
            if missing_date:
                report += "missing date(s) between files \"" + short_file_name + "\" and \"" + short_file_names[short_file_name_num + 1] + "\"\n"
    if report == "":
        report = "\n"
    f = open(out_path, "w")
    f.write(report)
    f.close()
