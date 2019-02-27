import numpy as np
import pandas as pd
import os
from scipy import signal
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.datasets import make_blobs
import DataSet as dt 

#OLS Ordinary Least Square : la régression linéaire 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
X, y = dt.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
lr = LinearRegression().fit(X_train, y_train)
#Affichage des coef 
print('********************************************')
print('Linear Model : \n')
print("coef : ",lr.coef_)
print("ordonne a l'origine : ", lr.intercept_)

#Ridge with default alpha = 1
from sklearn.linear_model import Ridge
ridge = Ridge().fit(X_train, y_train)
print('********************************************')
print('Ridge Model (alpha=1) : \n') 
print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))

#Lasso 
from sklearn.linear_model import Lasso

X, y = dt.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=38)

lasso001 = Lasso(alpha=0.01, max_iter=1000).fit(X_train, y_train)
print('********************************************')
print('Lasso Model (alpha=0.01) : \n') 
print("Training set score: {:.2f}".format(lasso001.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso001.score(X_test, y_test)))
print("Number of features used:", np.sum(lasso001.coef_ != 0))


