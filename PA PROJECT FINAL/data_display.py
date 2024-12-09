import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("obesity_data.csv")


X = data[['Sleep Duration', 'PhysicalActivity', 'Sugary Foods', 'fatty/oily foods', 'Soft drinks']]
y = data['BMI']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=100, random_state=42)


regression_model = LinearRegression()
regression_model.fit(X_train, y_train)


y_pred = regression_model.predict(X_test)


plt.figure(figsize=(10, 6))


plt.plot(y_test.values, color='blue', label='Actual Values')


plt.plot(y_pred, color='green', label='Predicted Values')

plt.xlabel('Index')
plt.ylabel('BMI')
plt.title('Actual vs Predicted BMI')
plt.legend()
plt.grid(True)
plt.show()

