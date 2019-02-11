# -*- coding: utf8 -*-
from __future__ import division
from pylab import *
from scipy.io.wavfile import read
from compute_onset import compute_onset
import random

def parse():
    wavs = {}  # (ID, file number): ((sample frequency, array), onset in seconds)
    #doesn't include slides with comments next to them
    f = open("/home/xander/Speech_Data/onset_times.csv")
    lines = f.readlines()
    f.close()
    for line in lines[1:-1]:
        parts = line.split(',')
        if " " not in parts[4]:
            file_n = int(parts[4])
        ID = int(parts[5])
        onset = float(parts[8])
        if parts[11] == "0":
            wav = read("/home/xander/Speech_Data/" + str(ID) + "/LetterNumber110716-" + str(ID) + "-1MixedBlock-" + str(file_n) + ".wav")
            wavs[(ID, file_n)] = (wav, onset)
    return wavs

def reject_outliers(data, radius = 10):
    sorted_data = sorted(data)
    best_start = 0
    best_len = 0
    current_start = 0
    current_end = 1
    while current_start < len(data):
        while current_end < len(sorted_data) and sorted_data[current_end] <= sorted_data[current_start] + 2 * radius / 1000:
            current_end += 1
        if current_end - current_start > best_len:
            best_start = current_start
            best_len = current_end - current_start
        current_start += 1
    return sorted_data[best_start: best_start + best_len]
        

def hist_bins(dividers, deltas):
    #dividers would be [5, 10, 25, 100]
    #to represent intervals [0, 5), [5, 10), ..., [100, float("inf"))
    new_dividers = [0,] + dividers
    bins = [0,]*len(new_dividers)
    for d in deltas:
        start = 0
        stop = len(new_dividers)
        middle = int((start + stop) / 2)
        while stop - start > 1:
            if d >= new_dividers[middle] / 1000: #1000 is to convert to milliseconds
                start = middle
            else:
                stop = middle
            middle = int((start + stop) / 2)
        bins[start] += 1
    return [b / len(deltas) for b in bins]

wavs = parse()
n_train = len(wavs) // 2
n_test = len(wavs) - n_train
train = sorted(random.sample(wavs.keys(), n_train))
test = sorted(list(set(wavs.keys()) - set(train)))

print "train = " + str(train)
print "test = " + str(test)

dividers = [5, 10, 25, 100]

deltas = []
for keynum, key in enumerate(train):
    print key,
    print int(100 * keynum / n_train),
    print "train"
    (sample_frequency, wav), onset = wavs[key]
    computed_onset = compute_onset(sample_frequency, wav, 2.35, durations = [(0, 0.5), (0.001, 0.2), (0.02, 1)], cutout=22)[0]
    deltas.append(computed_onset - onset)

deltas = array(deltas)
fil_delt = reject_outliers(deltas)
fil_avg = sum(fil_delt) / len(fil_delt)
deltas = abs(deltas - fil_avg)
print deltas
print hist_bins(dividers, deltas)

deltas = []
for keynum, key in enumerate(test):
    print key,
    print int(100 * keynum / n_test),
    print "test"
    (sample_frequency, wav), onset = wavs[key]
    computed_onset = compute_onset(sample_frequency, wav, 2.35, durations = [(0, 0.5), (0.001, 0.2), (0.02, 1)], cutout=22)[0]
    deltas.append(computed_onset - onset)

deltas = abs(array(deltas) - fil_avg)
print deltas
print hist_bins(dividers, deltas)
