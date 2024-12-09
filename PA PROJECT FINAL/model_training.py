import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np


data = pd.read_csv("obesity_data.csv")


X = data[['Sleep Duration', 'PhysicalActivity', 'Sugary Foods', 'fatty/oily foods', 'Soft drinks']]
y = data['BMI']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=100, random_state=42)




regression_model = LinearRegression()
regression_model.fit(X_train, y_train)


y_pred = regression_model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
accuracy = round(r2 * 100, 2)


coefficients = regression_model.coef_
intercept = regression_model.intercept_


categories = {
    (0, 18.5): "Underweight",
    (18.5, 24.9): "Normal weight",
    (25, 29.9): "Overweight",
    (30, np.inf): "Obese"
}
