# -*- coding: utf8 -*- 
from __future__ import division
from pylab import *
from scipy.signal import savgol_filter
import random
import os

def x_to_z(sample_frequency, x, new_power, durations, zero_window):
    zero_window_slides = int(sample_frequency * zero_window)
    neut_x = []
    pos = 0
    while pos < len(x):
        s = int(sum(x[pos: pos + zero_window_slides]) / min(zero_window_slides, len(x) - pos))
        for i in range(pos, min(len(x), pos + zero_window_slides)):
            neut_x.append(x[i] - s)
        pos += zero_window_slides
    ds = [int(sample_frequency * dur[0]) for dur in durations]
    tot_power = 0
    for dur in durations:
        tot_power += dur[1]
    frac = new_power / tot_power
    y = abs(array(neut_x, dtype=int))
    ends = []
    for d in ds:
        if d > 0:
            ends.append([-int(d/2), int(d/2) + 1])
        else:
            ends.append([0, 1])
    rolling_sums = [sum(y[0:en[1]]) for en in ends]
    z = []
    zlog = [0]
    for k in range(len(rolling_sums)):
        r = rolling_sums[k]
        if r > 0:
            zlog[0] += (frac * durations[k][1]
                     * log(r / (ends[k][1] - 0)))
        else:
            zlog[0] = -float("inf")
    z.append(e**zlog[0])
    for i in range(1, len(x)):
        for j in range(len(rolling_sums)):
            if ends[j][0] >= 0:
                rolling_sums[j] -= y[ends[j][0]]
            if ends[j][1] < len(x):
                rolling_sums[j] += y[ends[j][1]]
            ends[j][0] += 1
            ends[j][1] += 1
        zlog.append(0)
        for k in range(len(rolling_sums)):
            r = rolling_sums[k]
            if r > 0:
                zlog[i] += (frac * durations[k][1]
                         * log(r / (min(ends[k][1], len(x)) - max(ends[k][0], 0))))
            else:
                zlog[i] = -float("inf")
        z.append(e**(zlog[i]))
    return z

def compute_onset(sample_frequency,
                  x,
                  new_power = 2,
                  durations = [(0, 1), (1 / 10000, 1)],
                  min_start = 0.1,
                  min_len = 0.15,
                  cutout = 25,
                  zero_window = 0.01):
    z = x_to_z(sample_frequency, x, new_power, durations, zero_window)
    data_file = open("compute_onset_data.txt", "w")
    data_file.write(str(len(z[::cutout])) + " "
                  + str(int(min_start * sample_frequency / cutout)) + " "
                  + str(int(min_len * sample_frequency / cutout)) + "\n")
    for i in z[::cutout]:
        data_file.write(str(i) + "\n")
    data_file.close()
    os.system("./talk_interval.out")
    os.system("rm compute_onset_data.txt")
    ti_file = open("ti.txt")
    ti_file_lines = ti_file.readlines()
    ti_file.close()
    os.system("rm ti.txt")
    start_ti = int(ti_file_lines[0].split()[0])
    ratio = float(ti_file_lines[0].split()[2])
    return hone(sample_frequency, x, cutout*start_ti), ratio

def hone(sample_frequency, x, initial):
    #plot(x[initial - sample_frequency // 10: initial + sample_frequency // 10])
    #plot([sample_frequency // 10, sample_frequency // 10], [0, max(x)])
    #show()
    return initial / sample_frequency #coming back
