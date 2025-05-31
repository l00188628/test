from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

# Dummy training data
data = pd.DataFrame({
    'age': [21, 25, 30, 35, 40],
    'salary': [30000, 35000, 50000, 60000, 70000]
})

X = data[['age']]
y = data['salary']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')