import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import Regression as reg
from Regression import LinearRegression as linear
from Regression import RidgeRegression as ridge

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)

alphas = [.01, .05, .075, .1, .5, .75, 1, 5, 7.5, 10]
r2_list_ridge = []
r2_list_linear = []
r_reg = ridge()
l_reg = linear()
for alpha in alphas:
    #set the alpha for each model
    r_reg.set_params(alpha=alpha)
    l_reg.set_params(alpha=alpha)
    #fit both regression
    r_reg.fit(X_train, y_train)
    l_reg.fit(X_train, y_train)
    #score the models
    r_reg.score(X_test, y_test)
    l_reg.score(X_test, y_test)
    #append the scores to the list
    r2_list_ridge.append(r_reg.r_2)
    r2_list_linear.append(l_reg.r_2)

#Creating and labeling plot
plt.plot(alphas, r2_list_ridge, label = "Ridge Regression")
plt.plot(alphas, r2_list_linear, label = "Linear Regression")
plt.title('Comparing Ridge and Linear Regression for different Alpha Values')
plt.xlabel('Alpha Values')
plt.ylabel('R-squared Scores')
plt.legend()
plt.show()