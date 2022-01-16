import sklearn
from sklearn import linear_model
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from sklearn.metrics import mean_absolute_error


data = pd.read_csv("50_Startups.csv",sep = ",")
data = data[['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']]

find = "Profit"
inputs = np.array(data.drop([find],1))
outputs = np.array(data[find])

input_train,input_test,output_train,output_test = sklearn.model_selection.train_test_split(inputs,outputs,test_size = 0.2)

model = linear_model.LinearRegression()
model.fit(input_train,output_train)
acc = model.score(input_test,output_test)
print(acc)

ypred = model.predict(input_test)
ypred[:5]
output_test[:5]
model.score(input_test,output_test)

print(f'Model Score on Training Data: {round(model.score(input_train,output_train)*100,2)}%')
print(f'Model Score on Test Data: {round(model.score(input_test,output_test)*100,2)}%')

sns.set_style('whitegrid')
s = sns.scatterplot(x=output_test,y=ypred)

print('MAE:',mean_absolute_error(output_test,ypred))

pd.to_pickle(model, 'startup.pkl')

