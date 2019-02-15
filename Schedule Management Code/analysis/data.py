from __future__ import division
from pylab import *
import sys
import glob
from day_number import day_number

def __main__():
    """
    This function passes 
    off the gruntwork to either
    fulldata() or partdata(),
    depending on whether a start
    and stop date is specified.
    """
    if len(sys.argv) == 1:
        fulldata()
    else:
        partdata(sys.argv[1], sys.argv[2])

def fulldata():
    """
    This function plots the graphs
    and computes the statistics
    on the full dataset.
    """
    file_paths = glob.glob("../times/compiled/*")
    names = [file_path.split("/")[-1] for file_path in file_paths]
    names.sort(key=lambda name: day_number(name))
    totals = [] #a list of the amount of time spent each day for every day.
    for name in names:
        f = open("../times/compiled/" + name)
        lines = f.readlines()
        f.close()
        last_line = lines[-1]
        total = 0
        words = last_line.split(" ")
        for wordnum, word in enumerate(words):
            if word in ["minute", "minutes"]:
                total += int(words[wordnum - 1])
            elif word in ["hour", "hours"]:
                total += 60*int(words[wordnum - 1])
        totals.append(total)
    print_length(len(totals))
    print_average(int(round(sum(totals) / len(totals))))
    print_median(totals)
    print_first_quartile(totals)
    print_third_quartile(totals)
    print_max(max(totals))
    print_total(sum(totals))
    print_needed(totals)
    make_plots(totals)

def partdata(start, stop):
    """
    This function plots the graphs
    and computes the statistics
    on the dataset lying between
    the dates "start" and "stop".
    """
    file_paths = glob.glob("../times/compiled/*")
    names = [file_path.split("/")[-1] for file_path in file_paths]
    names.sort(key=lambda name: day_number(name))
    names = names[names.index(start): names.index(stop) + 1]
    totals = [] #a list of the amount of time spent each day for every day.
    for name in names:
        f = open("../times/compiled/" + name)
        lines = f.readlines()
        f.close()
        last_line = lines[-1]
        total = 0
        words = last_line.split(" ")
        for wordnum, word in enumerate(words):
            if word in ["minute", "minutes"]:
                total += int(words[wordnum - 1])
            elif word in ["hour", "hours"]:
                total += 60*int(words[wordnum - 1])
        totals.append(total)
    print_length(len(totals))
    print_average(int(round(sum(totals) / len(totals))))
    print_median(totals)
    print_first_quartile(totals)
    print_third_quartile(totals)
    print_max(max(totals))
    print_total(sum(totals))
    make_plots(totals)

def print_length(l):
    """
    This function prints
    the number of days worked in the
    specified interval,
    given that quantity as an int.
    """
    numweeks = l // 7
    leftover = l % 7
    if numweeks == 0:
    	if leftover == 0:
    		print "The inquired interval has length zero!"
    	elif leftover == 1:
    		print "The inquired interval has length 1 day."
    	else:
    		print "The inquired interval hsa length " + str(l) + " days."
    elif numweeks == 1:
    	if leftover == 0:
    		print "The inquired interval has length 1 week."
    	elif leftover == 1:
    		print "The inquired interval has length 1 week and 1 day."
    	else:
    		print "The inquired interval has length 1 week and " + str(leftover) + " days."
    else:
    	if leftover == 0:
    		print "The inquired interval has length " + str(numweeks) + " weeks."
    	elif leftover == 1:
    		print "The inquired interval has length " + str(numweeks) + " weeks and 1 day."
    	else:
    		print "The inquired interval has length " + str(numweeks) + " weeks and " + str(leftover) + " days."

def print_average(avg):
    """
    This function prints
    the average amount of work
    performed in the specific interval,
    given that quantity as an int in minutes.
    """
    hours = avg // 60
    minutes = avg % 60
    if hours == 0:
    	if minutes == 0:
    		print "In the specified interval, you haven't even been working an average of a minute a day!"
    	elif minutes == 1:
    		print "In the specified interval, you've been working an average of a minute per day."
    	else:
    		print "In the specified interval, you've been working an average of " + str(minutes) + " minutes per day."
    elif hours == 1:
    	if minutes == 0:
    		print "In the specified interval, you've been working an average of 1 hour a day."
    	elif minutes == 1:
    		print "In the specified interval, you've been working an average of 1 hour 1 minute per day."
    	else:
    		print "In the specified interval, you've been working an average of 1 hour " + str(minutes) + " minutes a day."
    else:
    	if minutes == 0:
    		print "In the specified interval, you've been working an average of " + str(hours) + " hours a day."
    	elif minutes == 1:
    		print "In the specified interval, you've been working an average of " + str(hours) + " hours 1 minute per day."
    	else:
    		print "In the specified interval, you've been working an average of " + str(hours) + " hours " + str(minutes) + " minutes a day." 

def print_median(totals):
    """
    This function prints the median amount
    of work, given the "totals" list.
    """
    datasorted = sorted(totals)
    middle = datasorted[len(datasorted) // 2]
    hours = middle // 60
    minutes = middle % 60
    if hours == 0:
            if minutes == 0:
                    print "In the specified interval, your median amount of work per day is nothing at all!"
            elif minutes == 1:
                    print "In the specified interval, your median amout of work is a measly 1 minute per day"
            else:
                    print "In the specified interval, your median work is " + str(minutes) + " minutes a day."
    elif hours == 1:
            if minutes == 0:
                    print "In the specified interval, your median work load is 1 hour a day."
            elif minutes == 1:
                    print "In the specified interval, your median work load is 1 hour 1 minute per day."
            else:
                    print "In the specified interval, your median work load is 1 hour " + str(minutes) + " minutes a day."
    else:
            if minutes == 0:
                    print "In the specified interval, your median work load is " + str(hours) + " hours a day."
            elif minutes == 1:
                    print "In the specified interval, your median work load is " + str(hours) + " hours 1 minute per day."
            else:
                    print "In the specified interval, your median work load is " + str(hours) + " hours " + str(minutes) + " minutes a day."

def print_first_quartile(totals):
    """
    This function prints the first quartile,
    given the totals list.
    """
    datasorted = sorted(totals)
    first_quartile = datasorted[len(datasorted) // 4]
    hours = first_quartile // 60
    minutes = first_quartile % 60
    if hours == 0:
            if minutes == 0:
                    print "In the specified interval, you haven't worked at all during at least one quareter of your logged days!"
            elif minutes == 1:
                    print "In the specified interval, one quarter of your days have only got one minute or less work logged."
            else:
                    print "In the specified interval, one quarter of your days have got " + str(minutes) + " minutes or less of work logged."
    elif hours == 1:
            if minutes == 0:
                    print "In the specified interval, one quarter of your days have got 1 hour or less work logged."
            elif minutes == 1:
                    print "In the specified interval, one quarter of your days have got 1 hour 1 minute or less work logged."
            else:
                    print "In the specified interval, one quarter of your days have got 1 hour " + str(minutes) + " minutes or less work logged."
    else:
            if minutes == 0:
                    print "In the specified interval, one quarter of your days have got " + str(hours) + " hours or less work logged."
            elif minutes == 1:
                    print "In the specified interval, one quarter of your days have got " + str(hours) + " hours one minute or less work logged."
            else:
                    print "In the specified interval, one quarter of your days have got " + str(hours) + " hours " + str(minutes) + " minutes or less work logged."

def print_third_quartile(totals):
    """
    This function prints the third quartile,
    given the totals list.
    """
    datasorted = sorted(totals)
    first_quartile = datasorted[(3 * len(datasorted)) // 4]
    hours = first_quartile // 60
    minutes = first_quartile % 60
    if hours == 0:
            if minutes == 0:
                    print "In the specified interval, you haven't worked at all during at least three quareters of your logged days!"
            elif minutes == 1:
                    print "In the specified interval, three quarters of your days have only got one minute or less work logged."
            else:
                    print "In the specified interval, three quarters of your days have got " + str(minutes) + " minutes or less of work logged."
    elif hours == 1:
            if minutes == 0:
                    print "In the specified interval, three quarters of your days have got 1 hour or less work logged."
            elif minutes == 1:
                    print "In the specified interval, three quarters of your days have got 1 hour 1 minute or less work logged."
            else:
                    print "In the specified interval, three quarters of your days have got 1 hour " + str(minutes) + " minutes or less work logged."
    else:
            if minutes == 0:
                    print "In the specified interval, three quarters of your days have got " + str(hours) + " hours or less work logged."
            elif minutes == 1:
                    print "In the specified interval, three quarters of your days have got " + str(hours) + " hours one minute or less work logged."
            else:
                    print "In the specified interval, three quarters of your days have got " + str(hours) + " hours " + str(minutes) + " minutes or less work logged."

def print_max(m):
    """
    This function prints the maximum,
    given that number as an int in minutes.
    """
    hours = m // 60
    minutes = m % 60
    if hours == 0:
    	if minutes == 0:
    		print "In the specified interval, you didn't work at all on record!"
    	elif minutes == 1:
    		print "In the specified interval, at most, you worked a hilariously minuscule minute per day!"
    	else:
    		print "In the specified interval, your record high for work is " + str(minutes) + " minutes per day."
    elif hours == 1:
    	if minutes == 0:
    		print "In the specified interval, your record high for work is 1 hour a day."
    	elif minutes == 1:
    		print "In the specified interval, your record high for work is 1 hour 1 minute per day."
    	else:
    		print "In the specified interval, your record high for work is 1 hour " + str(minutes) + " per day."
    else:
    	if minutes == 0:
    		print "In the specified interval, your record high for work is " + str(hours) + " hours per day."
    	elif minutes == 1:
    		print "In the specified interval, your record high for work is " + str(hours) + " hours 1 minute per day."
    	else:
    		print "In the specified interval, your record high for work is " + str(hours) + " hours " + str(minutes) + " minutes per day."

def print_total(t):
    """
    This function prints the total time
    worked, given that quantity in minutes.
    """
    hours = t // 60
    minutes = t % 60
    if hours == 0:
    	if minutes == 0:
    		print "In the specified interval, you don't seem to have worked at all!"
    	elif minutes == 1:
    		print "In the specified interval, you've only worked one mintue!"
    	else:
    		print "In the specified interval, you've worked a total of " + str(minutes) + " minutes."
    elif hours == 1:
    	if minutes == 0:
    		print "In the specified interval, you've worked a total of 1 hour."
    	elif minutes == 1:
    		print "In the specified interval, you've worked a total of 1 hour 1 minute."
    	else:
    		print "In the specified interval, you've worked a total of 1 hour " + str(minutes) + " minutes."
    else:
    	if minutes == 0:
    		print "In the specified interval, you've worked a total of " + str(hours) + " hours."
    	elif minutes == 1:
    		print "In the specified interval, you've worked a total of " + str(hours) + " hours 1 minute."
    	else:
    		print "In the specified interval, you've worked a total of " + str(hours) + " hours " + str(minutes) + " minutes."

def print_needed(totals):
    """
    This function prints the number of
    extra minutes needed to be worked in order to 
    increase the average time by one minute.
    """
    avg = sum(totals) / len(totals)
    new_average = int(round(avg))
    border = (2*new_average + 1) / 2
    difference = border - avg
    work = int(round(difference * len(totals)))
    hours = work // 60
    minutes = work % 60
    if hours == 0:
    	if minutes == 0:
    		print "You don't have to work at all for the average to increase by one minute!"
    	elif minutes == 1:
    		print "You have to work 1 more minute today for your average to increase by 1 minute."
    	else:
    		print "You have to work " + str(minutes) + " more minutes today for your average to increase by 1 minute."
    elif hours == 1:
    	if minutes == 0:
    		print "You have to work 1 more hour today for your average to increase by 1 minute."
    	elif minutes == 1:
    		print "You have to work 1 hour 1 minute more today for your average to increase by 1 minute."
    	else:
    		print "You have to work 1 hour " + str(minutes) + " minutes more today for your average to increase by 1 minute."
    else:
    	if minutes == 0:
    		print "You have to work " + str(hours) + " hours more today for your average to increase by 1 minute."
    	elif minutes == 1:
    		print "You have to work " + str(hours) + " hours 1 minute more today for your average to increase by 1 minute."
    	else:
    		print "You have to work " + str(hours) + " hours " + str(minutes) + " minutes more today for your average to increase by 1 minute."

def smooth(data, size):
    """
    This smooths out the data.
    "size" is the radius of smoothing.
    """
    new_data = []
    for inum in range(len(data)):
        bottom = max(inum - size, 0)
        top = min(inum + size, len(data) - 1)
        scale = top - bottom + 1
        new_data.append(sum(data[bottom: top + 1]) / scale)
    return new_data

def histogram(xs, spacing):
    """
    Counts the number of items in xs that fall into bins with spacing "spacing".
    We assume that xs does not contain any negative numbers.
    The function normalizes the output.
    """
    bins = int(max(xs) // spacing) + 1
    counts = [0 for i in range(bins)]
    for x in xs:
        index = int(x // spacing)
        counts[index] += 1
    return counts

def make_plots(totals):
    """
    This function performs all the plotting.
    """
    plot(totals)
    plot(smooth(totals, size = 2))
    plot(smooth(totals, size = 4))
    show()
    in_order = sorted(totals)
    xs = []
    ys = []
    for inum, i in enumerate(in_order):
    	ys.append(100 * (inum + 1) / len(in_order))
    	xs.append(i)
    plot(xs, ys)
    average_2_xs = smooth(xs, size = 2)
    average_4_xs = smooth(xs, size = 4)
    plot(average_2_xs, ys)
    plot(average_4_xs, ys)
    show()
    spacing = 30
    his = histogram(totals, spacing)
    xs = [spacing*i + spacing/2 for i, ivalue in enumerate(his)]
    plot(xs, his)
    show()

if __name__=="__main__":
    __main__()

