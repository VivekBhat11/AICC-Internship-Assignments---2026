"""
Assignment (09/03/2026)

Assignment Name : House Price Predictor
Description : Train a Linear Regression model, predict prices, and test with new input.


This program builds a house price prediction model using Linear Regression. The model is trained using sample data where input features (like size or number of rooms) are used to predict house prices. After training, the model can predict prices for new inputs. This demonstrates how machine learning models learn patterns and make predictions.


"""

from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset (Study hours vs house price - example)
X = np.array([[1], [2], [3], [4], [5]])   # Feature
y = np.array([100, 150, 200, 250, 300])   # Label (price)

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict price
prediction = model.predict([[6]])
print("Predicted Price:", prediction[0])