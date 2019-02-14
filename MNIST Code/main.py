from __future__ import division
from pylab import *
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from mnist import load_mnist

def one_to_many(n, most=10):
    return [i==n for i in range(most)]

DATA_SIZE = 100
COMPONENTS = 101

def preprocess(images):
    """
    This function takes as input
    images as load_mnist returns (without the labels)
    and returns the whitened data (an array
    of the arrays that will DIRECTLY be passed 
    into the neural net)
    """
    flattened_images = images.reshape(DATA_SIZE, images.shape[1] * images.shape[2])
    zero_mean_images = flattened_images - mean(flattened_images, axis=0)
    normalized_images = zero_mean_images / (std(zero_mean_images, axis=0) + 0.01)
    cov = dot(normalized_images.T, normalized_images) / normalized_images.shape[0]
    U,S,V = linalg.svd(cov)
    rot_reduced = dot(normalized_images, U[:,:COMPONENTS])
    white = rot_reduced / sqrt(S[:COMPONENTS] + 1e-5)
    return white

images, labels = load_mnist('training', selection=slice(0,DATA_SIZE))
test_images, test_labels = load_mnist('testing', selection=slice(0,DATA_SIZE))
net = buildNetwork(COMPONENTS, 1000, 500, 100, 10, bias=True)
data = SupervisedDataSet(COMPONENTS, 10)

white = preprocess(images)
test_white = preprocess(test_images)

for whitened, label in zip(white, labels):
    data.addSample(whitened, one_to_many(label))

vals = []
testing_vals = []

trainer = BackpropTrainer(net, data, learningrate=0.0001)
for epoch in range(200):
    print ""
    print epoch
    print trainer.train()
    correct = 0
    for i in range(DATA_SIZE):
        guessed = net.activate(test_white[i]).argmax()
        if guessed == test_labels[i]:
            correct += 1
    print "testing dataset = " + str(correct / DATA_SIZE)
    testing_vals.append(correct / DATA_SIZE)
    correct = 0
    for i in range(DATA_SIZE):
        guessed = net.activate(white[i]).argmax()
        if guessed == labels[i]:
            correct += 1
    print "training dataset = " + str(correct / DATA_SIZE)
    vals.append(correct / DATA_SIZE)
    print ""

plot(testing_vals)
show()
