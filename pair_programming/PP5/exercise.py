import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.weights = np.random.uniform(0, 1, self.shape[1])
        self.bias = np.random.uniform(0, 1, self.shape[0])

    def forward(self, inputs):
        self.output = self.actv(np.dot(inputs, self.weights) + self.bias)
        return self.output

    def __str__(self):
        return(f'The activation function is {self.actv} and the shape is {self.shape}')

    def __repr__(self):
        class_name = type(self).__name__
        return "%s(shape=%r, activation function=%r)" % (class_name, self.shape, self.actv)

    def __eq__(self, other):
        return (self.shape[0] == other.shape[1])


shape1 = (20,100)
shape2 = (3,20)
actv =  np.tanh       

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) 

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

print(layer1==layer2)