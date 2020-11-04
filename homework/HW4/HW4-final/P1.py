import numpy as np
import matplotlib.pyplot as plt

#declare auto d function
def numerical_diff(f, h):
    def input_value(x):
        nonlocal h
        nonlocal f
        return (f(x+h) - f(x))/h
    return input_value


#Establish x and h values
x = np.linspace(.2, .4, 50)
h_list = [10**-1, 10**-7, 10**-15]

h_dict = {}

#evaluate derivatives for different h and x values
for h in h_list:
    h_dict[h] = []
    diff = numerical_diff(np.log, h)
    for val in x:
        h_dict[h].append(diff(val))

#create analytical derivative and plot it
plt.plot(x, 1/x, label='analytical', linewidth = 5, c='b')
#plot the derivatives with derrent values of h
plt.plot(x,h_dict[10**-1], label = 'h = 1e-1', c='g')
plt.plot(x,h_dict[10**-7], '--', label = 'h = 1e-7', c= 'r')
plt.plot(x,h_dict[10**-15], label = 'h = 1e-15', c='y')
plt.xlabel('Values for Derivative Evaluation')
plt.ylabel('Derivative Value')
plt.title('Evaluating Derivatives Numerically with Different h Values')
plt.legend()



print('Answer to Q-a: The most accurate value of h is 10e-7. When h is too small,\
    it is innaccurate because of the issues machine precision. When h is too big, the estimation is not accurate')

print('Answer to Q-b: Automatic differentiaion helps address these problems because it removes h from the equation. \
    So, we will not have eproblems with machine precision nor innacuracy due to large h - no parameter necessary. This happens because we continuously \
        recursively take the analytical derivative of the "sub" functions of the main function we try to evaluate')

plt.show()
