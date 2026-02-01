import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("house_data.csv")

# Input features
X = data[['area', 'bedrooms', 'bathrooms']]

# Output (price)
y = data['price']

# Create & train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("house_model.pkl", "wb"))

print("Model trained successfully")
