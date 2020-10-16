import numpy as np

def my_pow(r):
    return np.power(3,r), r*np.power(3,r-1)

def my_pow(r):
    def forward(structure):
        nonlocal r
        return np.power(structure,r), r*np.power(structure,r-1)
    return forward

class auto():
    def __init__(self, structure):
        self.structure = structure

    def __pow__(self, r):
        return np.power(self.structure,r), r*np.power(self.structure,r-1)



if __name__ == "__main__":
    diff = auto(3)
    diff**4
    print(diff**4)