from __future__ import division
from pylab import *
from scipy.io.wavfile import read, write
from time import sleep
import os

wav = read("/home/xander/Speech_Data/1847/LetterNumber110716-1847-1MixedBlock-12.wav")
#new_wav = []
#for i in range(0, len(wav[1]) - 15000, 15000):
#    f = rfft(wav[1][i: i + 15000], norm="ortho")
#    g = [f[j] if j < 50000 else 0 for j in range(len(f))]
#    new_wav += list(irfft(g, norm="ortho"))
##note to self: must convert elements of new_wav to int before playing
r = rfft(wav[1], norm="ortho")
g = [r[j] if 50 * (len(r) / 750) < j < 200 * (len(r) / 750) else 0 for j in range(len(r))]
new_wav = rint(array(irfft(g, norm="ortho"))).astype(int16)
print wav[1][:15]
print new_wav[:15]
print wav[0]
print type(new_wav[0])
write("/home/xander/Speech_Data/listen_output.wav", wav[0], new_wav)
os.system("play /home/xander/Speech_Data/listen_output.wav")
