#Consider the data from the file weight-height.csv.
#1) Inspect the dependence between height and weight using a scatter plot. You may use either of the variables as independent variable.
#2) Choose appropriate model for the dependence
#3) Perform regression on the data using your model of choice
#4) Plot the results
#5) Compute RMSE and R2 value
#6) Assess the quality of the regression (visually and using numbers) in your own words.
#You are not required to split the dataset into training and testing sets. Of course you are completely free to experiment it here already.
#It is recommended that you use the module sklearn for all your computations.

import pandas as pd
import matpotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv(r'C:\***\weight.csv')

plt.scatter(data['Height'], data['Weight'])
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.show()

x = data[['Height']]
y = data['Weight']

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred, color='yellow')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.show()

rmse = mean_squared_error(y, y_pred, squared=False)

print(data.head())
print(data.info))
print(data.shape())
print(data.columns())
print(data.describe())
print(data.isnull().sum())


 
