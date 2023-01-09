# Import required libraries
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Load the stock data
data = pd.read_csv("stock_data.csv")

# Clean the data by removing missing values
data = data.dropna()

# Extract the closing prices and convert them to a numpy array
closing_prices = data["Close"].to_numpy()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    closing_prices, closing_prices, test_size=0.2)

# Train a support vector regression model on the training data
model = SVR(kernel="linear")
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model's performance using mean squared error
mse = np.mean((predictions - y_test)**2)
print("Mean squared error:", mse)

# Use the trained model to make predictions on new data
new_data = [100, 200, 300, 400]
predictions = model.predict(new_data)
print("Predictions:", predictions)
