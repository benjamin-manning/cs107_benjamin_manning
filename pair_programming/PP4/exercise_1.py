import numpy as np
def layer(shape, actv):
    def inner(inputs, weights, bias):
        return actv(np.dot(weights,inputs) + bias)
    return inner

t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) 

layer1 = layer(np.array([len(t),2]), np.tanh)
layer2 = layer(np.array([len(t),3]), np.tanh)

w1 = np.random.uniform(0.0, 1.0, len(t)).reshape(-1,1)
w2 = np.random.uniform(0.0, 1.0, len(t)).reshape(-1,1)
b1 = 2
b2 = 3

h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer
print(h2)
