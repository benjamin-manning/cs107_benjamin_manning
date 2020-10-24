#Creating the toy auto diff class
class AutoDiffToy():

    #initialization assuming that the derivative = 1
    def __init__(self, val, der = 1):
        self.val = float(val)
        self.der = float(der)
    
    #defining add accepting a class instance or a constant
    def __add__(self, other):
        try:
            return AutoDiffToy(self.val+other.val, self.der+other.der)
        except AttributeError:
            return AutoDiffToy(self.val+other, self.der)

    #allowing reversal
    def __radd__(self, other):
        return self.__add__(other)

    #setting up multiplication  - will not accept other class instance, must be constat
    def __mul__(self, other):
            return AutoDiffToy(self.val*other, self.der*other)

    #allowing reversal
    def __rmul__(self, other):
        return self.__mul__(other)


#establish all the parameters
a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)
alpha = 2.0
beta = 3.0

#Running all 4 test cases
f = alpha * x + beta
print(f.val,f.der)
f = x*alpha + beta
print(f.val,f.der)
f = beta + alpha * x
print(f.val,f.der)
f = beta + x*alpha
print(f.val,f.der)