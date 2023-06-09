# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XVD0_7TF7nM-G5HW1bqCjM2b_7Oh22WL
"""

import pandas as pd
import numpy as np
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

!ls /content/drive/MyDrive

insurance = pd.read_csv('/content/drive/MyDrive/insuranceSAD.csv')

insurance

import matplotlib.pyplot as plt

insurance[['age', 'bmi','charges']].describe()

fig, ax = plt.subplots(figsize=(16,7))

ax.hist(insurance['charges'], bins=10, alpha=0.5)

# histogram
# -> bins: liczba słupków
# -> alpha: transparentność

ax.set_xlabel('Charges')
ax.set_ylabel('Liczba obserwacji')

plt.show()

fig, ax = plt.subplots(figsize=(16,7))

ax.boxplot(insurance['charges'].dropna())

ax.set_ylabel('Charges')

plt.show()

fig, ax = plt.subplots(figsize=(16,7))


ax.hist(insurance.loc[insurance['smoker']==0, 'charges'], bins=10, alpha=0.5, label = 'nie palacy')
ax.hist(insurance.loc[insurance['smoker']==1, 'charges'], bins=10, alpha=0.5, label = 'palacy')

ax.set_xlabel('Wiek')
ax.set_ylabel('Liczba obserwacji')
ax.legend()

plt.show()

fig, ax = plt.subplots(figsize=(16,7))

ax.boxplot([insurance.loc[insurance['female']==0, 'charges'].dropna(),
           insurance.loc[insurance['female']==1, 'charges'].dropna()])

ax.set_ylabel('Wiek')

plt.show()

sns.countplot(x='children',
              data = insurance)

plt.show()

plt.figure(figsize=(10, 8))

# wizualizacja Heatmapy korelacji
ax = sns.heatmap(insurance.corr(),
                 xticklabels=insurance.corr().columns,
                 yticklabels=insurance.corr().columns, 
                 cmap='RdYlGn', 
                 vmin=-1, vmax=1,
                 annot=True, center=0)

# dekoracja wykresu
plt.title('Macierz korelacji dla wszystkich zmiennych', fontsize=20)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.25, top - 0.25) # odsunięcie etykiet od wykresu

# Zmiana wymiaru etykiet
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.show()

X = insurance[['bmi', 'age']]
Y = insurance[['charges']]

X.shape

Y.shape

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

for subset in [X, Y, X_train, Y_train, X_test, Y_test]:
    print(subset.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,Y_train)

model.coef_

model.intercept_

Y_predict_train = model.predict(X_train)
Y_predict_test = model.predict(X_test)

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

R2_train = r2_score(y_true = Y_train, y_pred = Y_predict_train)
R2_test = r2_score(y_true = Y_test, y_pred = Y_predict_test)

MAE_train = mean_absolute_error(y_true = Y_train, y_pred = Y_predict_train)
MAE_test = mean_absolute_error(y_true = Y_test, y_pred = Y_predict_test)

MSE_train = mean_squared_error(y_true = Y_train, y_pred = Y_predict_train)
MSE_test = mean_squared_error(y_true = Y_test, y_pred = Y_predict_test)

RMSE_train = mean_squared_error(y_true = Y_train, y_pred = Y_predict_train, squared = False)
RMSE_test = mean_squared_error(y_true = Y_test, y_pred = Y_predict_test, squared = False)

print(f'''R2_train = {R2_train},     R2_test = {R2_test},
MAE_train = {MAE_train},    MAE_test = {MAE_test},
MSE_train = {MSE_train},    MSE_test = {MSE_test},
RMSE_train = {RMSE_train},    RMSE_test = {RMSE_test} ''')

