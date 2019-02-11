from __future__ import division
from pylab import *

def evolve(params, devs, frac=0.2):
    #params should be sorted
    #from best to worst
    new_states = int(frac*len(params))
    new_params = []
    for i in range(new_states):
        a = int(random() * (len(params) - new_states))
        b = int(random() * (len(params) - new_states))
        if b == a and a > 0:
            b = a - 1 #anything will do
        elif b == a:
            b = 1 #assumes params has length at least 2
        new_param = []
        for j in range(len(devs)):
            new_param.append(max(0, (params[a][j] + params[b][j]) / 2 + normal(0, devs[j], 1)[0]))
        new_params.append(new_param)
    return params[:len(params) - new_states] + new_params
