# -*- coding: utf8 -*-
from __future__ import division
from pylab import *
from scipy.io.wavfile import read
from compute_onset import compute_onset
from evolve import evolve
#from old_onset import compute_onset
import random

def filename_to_number(f):
    start_flag = "C:\Users\Matt\Desktop\dummy wav"
    start_flag += "\NumberShape110716-7777-1MixedBlock-"
    stop_flag = '.wav'
    return int(f[len(start_flag):-len(stop_flag)])


def number_to_filename(n):
    return './source/NumberShape110716-7777-1MixedBlock-'+str(n)+'.wav'


def parse():
    # ignores files 2-4 because matt named them inconsistently
    # keys = range(5, 133)
    wavs = {}  # number: ((sample frequency, array), onset in seconds)
    with open('source/rt data for david.csv') as f:
        lines = f.readlines()
    for line in lines:
        parts = line.split(',')
        matt_path = parts[0]
        onset = float(parts[3])
        number = filename_to_number(matt_path)
        david_path = number_to_filename(number)
        wav = read(david_path)
        wavs[number] = wav, onset
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

list_of_best_bins = []
dividers = [5, 10, 25, 100]
list_of_best_settings = []
list_of_fil_avgs = []
devs = [0.075, 0.05, 0.05, 0.05] #these can be tweaked

for iteration in range(10):
    best_setting = [0, 0, 0, 0] 
    #the settings are:
    #power - float
    #durations[0][1] - float
    #durations[1][1] - float
    #durations[2][1] - float
    #cutout - int
    best_new_power_bins = [0, 0, 0, 0, 1]
    best_fil_avg = 0
    
    wavs = parse()
    new_wavs = {}
    for wav_key in wavs:
        if wav_key < 100: #this cirvuments the 101 / 102 bad test data
            new_wavs[wav_key] = wavs[wav_key]
    n_train = len(new_wavs) // 2
    n_test = len(new_wavs) - n_train
    train = sorted(random.sample(new_wavs.keys(), n_train))
    test = sorted(list(set(new_wavs.keys()) - set(train)))

    print "iteration = " + str(iteration)
    print "train = " + str(train)
    print "test = " + str(test)
    
    params = []
    scores = [] #we want a low score
    fas = []
    for x in range(10): #10 = number of states considered at one time
        new_param = []
        new_param.append(1.25 + 2 * random.random())
        new_param.append(random.random())
        new_param.append(random.random())
        new_param.append(random.random())
        params.append(new_param)

    for p in params:
        print p
        deltas = []
        for key in train:
            print key
            (sample_frequency, wav), onset = wavs[key]
            computed_onset = compute_onset(sample_frequency, wav, p[0], durations = [(0, p[1]), (0.001, p[2]), (0.02, p[3])], cutout=22)[0]
            deltas.append(computed_onset - onset)
        
        deltas = array(deltas)
        fil_delt = reject_outliers(deltas)
        fil_avg = sum(fil_delt) / len(fil_delt)
        fas.append(fil_avg)
        deltas = abs(deltas - fil_avg)
        p_bins = hist_bins(dividers, deltas)
        print p_bins
        new_score = p_bins[4] + 0.7 * p_bins[3] + 0.4 * p_bins[2] + 0.1 * p_bins[1] + 0.0035 * random.random()
        print new_score
        scores.append(new_score)
    
    params = [x for (y, x) in sorted(zip(scores, params), key=lambda pair: pair[0])]
    fas = [x for (y, x) in sorted(zip(scores, fas), key=lambda pair: pair[0])]
    scores.sort()

    print '--- evolving ---'

    for ev in range(7):
        print ev
        print params
        print devs
        print fas
        print scores
        params = evolve(params, devs, frac=0.5)
        print params
        for ev_pos in range(len(params) - int(0.5*len(params)), len(params)):
            print ev_pos
            print params[ev_pos]
            p = params[ev_pos]
            deltas = []
            for key in train:
                print key
                (sample_frequency, wav), onset = wavs[key]
                computed_onset = compute_onset(sample_frequency, wav, p[0], durations = [(0, p[1]), (0.001, p[2]), (0.02, p[3])], cutout=22)[0]
                deltas.append(computed_onset - onset)
            
            deltas = array(deltas)
            fil_delt = reject_outliers(deltas)
            fil_avg = sum(fil_delt) / len(fil_delt)
            fas[ev_pos] = fil_avg
            deltas = abs(deltas - fil_avg)
            p_bins = hist_bins(dividers, deltas)
            new_score = p_bins[4] + 0.7 * p_bins[3] + 0.4 * p_bins[2] + 0.1 * p_bins[1] + 0.0035 * random.random()
            scores[ev_pos] = new_score

        params = [x for (y, x) in sorted(zip(scores, params), key=lambda pair: pair[0])]
        fas = [x for (y, x) in sorted(zip(scores, fas), key=lambda pair: pair[0])]
        scores.sort()

        
    deltas = []
    for key in test:
        (sample_frequency, wav), onset = wavs[key]
        computed_onset = compute_onset(sample_frequency, wav, params[0][0], durations = [(0, params[0][1]), (0.001, params[0][2]), (0.02, params[0][3])], cutout=22)[0]
        deltas.append(computed_onset - onset)
    
    deltas = abs(array(deltas) - fas[0])

    print "\n\n\n\n\n"
    print "iteration = " + str(iteration)
    print "params[0] = " + str(params[0])
    bns = hist_bins(dividers, deltas)
    print "bns = " + str(bns)
    list_of_best_bins.append(bns)
    list_of_best_settings.append(params[0])
    list_of_fil_avgs.append(fas[0])

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print "list of best bins = " + str(list_of_best_bins)
avg_best_bins = array([0.0,]*(len(dividers) + 1))
for lobb in list_of_best_bins:
    avg_best_bins += array(lobb)
avg_best_bins = list(avg_best_bins / len(list_of_best_bins))
print "average best bins = " + str(avg_best_bins)
print "list of best settings = " + str(list_of_best_settings)
print "list of fil avgs = " + str(list_of_fil_avgs)
