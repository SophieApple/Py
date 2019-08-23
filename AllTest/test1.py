import sys,os,random
import numpy as np


def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))


class NetWork():
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x)
                        for (x,y) in zip(sizes[:-1],sizes[1:])]


    def feedforward(self,a):
        """Return the output of the network if 'a' is input."""
        for b,w in zip(self.biases,self.weights):
            a = sigmoid(np.dot(w,a)+b)
        return a

    def SGD(self,training_data,epochs,
            mini_batch_size,eta,test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent"""














if __name__ == '__main__':
    a = NetWork([12,3,2])
    print(a.feedforward([1,1,1,1,1,1,1,1,1,1,1,1]))

