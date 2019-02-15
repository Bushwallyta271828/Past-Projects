from __future__ import division
from numpy import *
from pylab import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(10, 1)
net = buildNetwork(10, 100, 10, 1)

for i in range(100):
    a = [(random() > 0.5) for j in range(10)]
    value = (sum(a) > 5)
    ds.addSample(a, (value,))

trainer = BackpropTrainer(net, ds)
ilist = range(500)
tlist = []
for i in ilist:
    err = trainer.train()
    tlist.append(log(err))
    print str(i) + " : " + str(err)
plot(ilist, tlist)
show()

correct = 0
for i in range(1000):
    a =  [(random() > 0.5) for j in range(10)]
    value = (sum(a) > 5)
    estimation = (net.activate(a)  > 0.5)
    if value == estimation:
        correct += 1/1000
print "correct = " + str(correct)