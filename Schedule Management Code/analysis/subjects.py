from __future__ import division
from pylab import *
import sys
import glob
import TimeClass
from day_number import day_number

def print_total(time, f):
    """
    This function writes to file the total
    amount of time spent working in the requested
    interval. "time" is a time object that
    stores the amount of time spent in the interval.
    "f" is an open file that will be written to.
    """
    hours, minutes = time.get_time()
    if hours == 0:
        if minutes == 0:
            f.write("You haven't worked at all in this interval!\n")
        elif minutes == 1:
            f.write("You've worked a total of 1 minute in this interval.\n")
        else:
            f.write("You've worked a total of " + str(minutes) + " minutes in this interval.\n")
    elif hours == 1:
        if minutes == 0:
            f.write("You've worked a total of 1 hour in this interval.\n")
        elif minutes == 1:
            f.write("You've worked a total of 1 hour 1 minute in this interval.\n")
        else:
            f.write("You've worked a total of 1 hour " + str(minutes) + " minutes in this interval.\n")
    else:
        if minutes == 0:
            f.write("You've worked a total of " + str(hours) + " hours in this interval.\n")
        elif minutes == 1:
            f.write("You've worked a total of " + str(hours) + " hours 1 minute in this interval.\n")
        else:
            f.write("You've worked a total of " + str(hours) + " hours " + str(minutes) + " minutes in this interval.\n")
        

def print_subject(subject, time, f):
    """
    This function writes to file the amount of
    time spent on a subject. "subejct" is a string
    containing the subject's name. "time" is a time 
    object that stores the amount of time spent on the subject.
    "f" is an open file (therefore it has an f.write(text)
    method) that will be written to.
    """
    hours, minutes = time.get_time()
    if hours == 0:
        if minutes == 0: f.write("    You have not worked on "
                               + subject + " on record.\n")
        elif minutes == 1: f.write("    You have worked 1 minute on "
                                 + subject + " on record.\n")
        else: f.write("    You have worked " + str(minutes) + " minutes on "
                    + subject + " on record.\n")
    elif hours == 1:
        if minutes == 0: f.write("    You have worked 1 hour on "
                               + subject + " on record.\n")
        elif minutes == 1: f.write("    You have worked 1 hour 1 minute on "
                                 + subject + " on record.\n")
        else: f.write("    You have worked 1 hour " + str(minutes) + " minutes on "
                    + subject + " on record.\n")
    else:
        if minutes == 0: f.write("    You have worked " + str(hours) + " hours on "
                               + subject + " on record.\n")
        elif minutes == 1: f.write("    You have worked " + str(hours) + " hours 1 minute on "
                                 + subject + " on record.\n")
        else: f.write("    You have worked " + str(hours) + " hours " + str(minutes) + " minutes on "
                    + subject + " on record.\n")

def print_tag(tag, time, f):
    """
    This function writes to file the amount of
    time spent on a tag. "tag" is the name of the tag
    in question. "time" is the amount of time spent on the tag
    in total, as a TimeClass.Time object. "f" is the file to write to.
    """
    hours, minutes = time.get_time()
    if hours == 0:
        if minutes == 0: f.write("For the " + tag + " tag: (no time spent working total)\n")
        elif minutes == 1: f.write("For the " + tag + " tag: (1 minute spent working total)\n")
        else: f.write("For the " + tag + " tag: (" + str(minutes) + " minutes spent working total)\n")
    elif hours == 1:
        if minutes == 0: f.write("For the " + tag + " tag: (1 hour spent working total)\n")
        elif minutes == 1: f.write("For the " + tag + " tag: (1 hour 1 minute spent working total)\n")
        else: f.write("For the " + tag + " tag: (1 hour " + str(minutes) + " minutes spent working total)\n")
    else:
        if minutes == 0: f.write("For the " + tag + " tag: (" + str(hours) + " hours spent working total)\n")
        elif minutes == 1: f.write("For the " + tag + " tag: (" + str(hours) + " hours 1 minute spent working total)\n")
        else: f.write("For the " + tag + " tag: (" + str(hours) + " hours " + str(minutes) + " minutes spent working total)\n")

def __main__():
    """
    This is the function that gets called
    when the program is run.
    """
    file_paths = glob.glob("../times/compiled/*")
    if len(sys.argv) == 3: #Do part-data work...
        names = [file_path.split("/")[-1] for file_path in file_paths]
        start = sys.argv[1]
        stop = sys.argv[2]
        names.sort(key=lambda name: day_number(name))
        names = names[names.index(start): names.index(stop) + 1]
        file_paths = ["../times/compiled/" + name for name in names]
    times = {}
    for file_path in file_paths:
        f = open(file_path)
        lines = f.readlines()
        f.close()
        if len(lines) > 1: #"f" shouldn't read, "Nothing done today."
            for line in lines[:-2]:
                hours = 0
                minutes = 0
                divide = line.index(" of ")
                subject = line[divide + 4:][:-2]
                time_line = line[:divide]
                words = time_line.split(" ")
                for wordnum, word in enumerate(words):
                    if word in ["hours", "hour"]: hours = int(words[wordnum - 1])
                    elif word in ["minutes", "minute"]: minutes = int(words[wordnum - 1])
                if subject in times: times[subject].compound(minutes, hours)
                else:
                    subject_timer = TimeClass.Time()
                    subject_timer.set_values(hours, minutes)
                    times[subject] = subject_timer
    tags = glob.glob("./tags/*")
    tag_map = {}
    tagged = set()
    for tag in tags:
        tag_name = tag.split("/")[-1]
        tag_file = open(tag)
        lines = tag_file.readlines()
        tag_file.close()
        tag_map[tag_name] = [line[:-1] for line in lines]
    output = open("SubjectTimes.txt", "w")
    total_time = TimeClass.Time()
    for subject in times:
        subject_time = times[subject]
        hours, minutes = subject_time.get_time()
        total_time.compound(minutes, hours)
    print_total(total_time, output)
    output.write("\n")
    for tag in tag_map:
        timer = TimeClass.Time()
        for subject in tag_map[tag]:
            if subject in times:
                subject_hours, subject_minutes = times[subject].get_time()
                timer.compound(subject_minutes, subject_hours)
        if timer.get_time()[0] > 0 or timer.get_time()[1] > 0: #If some subject in the tag is logged...
            print_tag(tag, timer, output)
            for subject in tag_map[tag]:
                if subject in times:
                    tagged.add(subject)
                    print_subject(subject, times[subject], output)
            output.write("\n")
    timer = TimeClass.Time()
    for subject in times:
        if subject not in tagged:
            subject_hours, subject_minutes = times[subject].get_time()
            timer.compound(subject_minutes, subject_hours)
    if timer.get_time()[0] > 0 or timer.get_time()[1] > 0:
        print_tag("Other", timer, output)
        for subject in times:
            if subject not in tagged:
                print_subject(subject, times[subject], output)
    output.close()

if __name__=="__main__":
    __main__()
