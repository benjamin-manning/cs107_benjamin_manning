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
alpha = 0.1
#set the models and their names
models = [linear(alpha), ridge(alpha)]
model_names = ['Linear Model', 'Ridge Model']
index=0

for model in models:
    model.fit(X_train, y_train)
    print(f'The {model_names[index]} coeffeficients are:')
    model.get_params()
    print(f'The R-squared for the {model_names[index]} is: {model.score(X_test, y_test)}')
    index+=1
