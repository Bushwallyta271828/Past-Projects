from __future__ import division
from pylab import *
from scipy.io.wavfile import read
from time import sleep

def n(l):
    s = 0
    for i in l:
        s += int(abs(i)) * int(abs(i))
    return s

wav = read("/home/xander/Speech_Data/1847/LetterNumber110716-1847-1MixedBlock-47.wav")
print wav
a = []
b = []
c = []
for i in range(0, len(wav[1]) - 1500, 200):
#    print i / wav[0], "-", (i + 1500) / wav[0]
    f = list(rfft(wav[1][i: i + 1500], norm="ortho"))
#    plot(abs(f))
    g = [f[j] if 75 < j < 200 else 0 for j in range(len(f))]
#    plot(abs(g))
    a.append(n(g))
    b.append(n(f))
    c.append(n(wav[1][i: i + 1500]))
    #print abs(wav[1][i: i + 1500])**2
#    show(block=False)
#    sleep(1)
#    close("all")
#    new_wav = irfft(g, norm="ortho")
#    plot(wav[1][i: i + 1500])
#    plot(new_wav)
#    show(block=False)
#    sleep(1)
#    close("all")

plot(array(a) / sum(a))
plot(array(b) / sum(b))
plot(array(c) / sum(c))
show()
