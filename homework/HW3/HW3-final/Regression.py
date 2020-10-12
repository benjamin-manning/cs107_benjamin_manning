import numpy as np
from numpy import transpose, dot, ones, hstack, identity
from numpy.linalg import pinv
from sklearn import datasets
#from sklearn.linear_model import LinearRegression as lr
#from sklearn.linear_model import Ridge
#from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


class Regression():
    def __init__(self):
        #Creating empty parameters dictionary
        self.params = {}

    def get_params(self):
        #Checking to see if there are any parameters in the model
        if not bool(self.params):
            raise Exception('No Parameters in the model yet')
        #Returning model parameters if they exist
        else:
            return self.params

    def set_params(self, **kwargs):
        #Put any new parameters in the dictionary
        for key in kwargs.keys():
            self.params[key] = kwargs[key]

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError
        # your code

    def score(self, X, y):
        raise NotImplementedError


class LinearRegression(Regression):
    def __init__(self, alpha=None):
        super(LinearRegression,self).__init__()
        self.params['alpha'] = alpha

    def fit(self, X, y):
        #Converiting to Numpy arrays
        X = np.array(X)
        y = np.array(y)
        #adding column of ones
        X = hstack((ones([X.shape[0],1]),X))
        #getting X transpose
        X_t = X.transpose()
        #Calculating the Betas
        betas = dot(pinv(dot(X_t,X)),dot(X_t,y))
        #store coefficients and intercept
        self.params['coefficients'] = betas[1:]
        self.params['intercept'] = betas[0]

    def predict(self, X):
        #Make sure X is a numpy array
        X = np.array(X)
        #calculate the predicted y values
        y_hat = dot(X,self.params['coefficients']) + self.params['intercept']
        return y_hat

    def score(self, X, y):
        #Converiting to Numpy arrays
        X = np.array(X)
        y = np.array(y)
        #Calculating the R^2 terms
        SSe = sum((y - self.predict(X))**2)
        SSt = sum((y - np.mean(y))**2)
        self.r_2 = 1 - SSe/SSt
        return self.r_2

    def __str__(self):
        return(f'The parameters are {self.params}')

class RidgeRegression(LinearRegression):
    def __init__(self, alpha=0):
        super(RidgeRegression,self).__init__()
        self.params['alpha'] = alpha

    def fit(self, X, y):
        #Converiting to Numpy arrays
        X = np.array(X)
        y = np.array(y)
        #adding column of ones
        X = hstack((ones([X.shape[0],1]),X))
        #getting X transpose
        X_t = X.transpose()
        #calculating gamma
        gamma = dot(self.params['alpha'], identity(X.shape[1]))
        #gamme Transpose
        gamma_t = gamma.transpose()
        #calculating betas
        betas = dot(pinv(dot(X_t,X) + dot(gamma_t,gamma)),dot(X_t,y))
        #store coefficients and intercept
        self.params['coefficients'] = betas[1:]
        self.params['intercept'] = betas[0]
