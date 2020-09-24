# The Perceptron Algorithm


# What is a Perceptron

# A Perceptron is an algorithm used for supervised learning of binary 
# classifiers. Binary classifiers decide whether an input, usually 
# represented by a series of vectors, belongs to a specific class.

# In short, a perceptron is a single-layer neural network. They consist 
# of four main parts including input values, weights and bias, 
# net sum, and an activation function.


# How does a perceptron work?

# The process begins by taking all the input values and multiplying 
# them by their weights. Then, all of these multiplied values are added 
# together to create the weighted sum. The weighted sum is then applied
# to the activation function, producing the perceptron's output. The 
# activation function plays the integral role of ensuring the output is 
# mapped between required values such as (0,1) or (-1,1). It is important 
# to note that the weight of an input is indicative of the strength of a 
# node. Similarly, an input's bias value gives the ability to shift the 
# activation function curve up or down.


# Perceptrons and ML

# As a simplified form of a neural network, specifically a single-layer 
# neural network, perceptrons play an important role in binary classification.
# This means the perceptron is used to classify data into two parts, hence 
# binary. Sometimes, perceptrons are also referred to as linear binary 
# classifiers for this reason.


import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self.unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init weights
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i  > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx,x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y_[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)



