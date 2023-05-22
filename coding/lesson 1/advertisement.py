import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Advertising.csv')

sns.scatterplot(data=df, x='TV', y='Sales')
plt.show()


X = df[['TV']].values
y = df['Sales'].values
reg = LinearRegression()
reg.fit(X,y)


y_pred = reg.predict(X)
plt.figure()
sns.scatterplot(data=df, X='TV' , y='Sales')
plt.plot(X, y_pred)
plt.show()
