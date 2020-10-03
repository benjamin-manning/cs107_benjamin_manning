import numpy as np
from numpy import transpose
from numpy.linalg import inv
from numpy import dot


class Regression():
    def __init__(self):
        self.params = {}

    def get_params(self):
        if not bool(self.params):
            return('You must fit a model before getting the parameters')
        else:
            return self.params

    def set_params(self, **kwargs):
        raise NotImplementedError

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.X_t = transpose(self.X)
        self.intercept = dot(dot(inv(dot(self.X_t, self.X)), self.X_t), self.y)[0]
        self.betas = dot(dot(inv(dot(self.X_t, self.X)), self.X_t), self.y)[1:]
        self.params['coefficients'] = self.betas
        self.params['intercept'] = self.intercept

    def predict(self, X):
        self.y_hat = dot(X, self.betas) + self.intercept
        return self.y_hat
        # your code

    def score(self, X, y):
        self.X = X
        self.y = y
        self.SSe = sum((self.y - predict(self.X))**2)
        self.SSt = sum((self.y - mean(self.y))**2)
        self.r_squared = 1 - self.SSe/self.SSt
        return self.r_squared


print(dir(Regression()))