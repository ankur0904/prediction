# price = 3 * x + 4 * y + 5 * z + 78
import numpy as np
from sklearn.linear_model import LinearRegression
from project_data import x, y
# Create some sample data

# Create a linear regression model
model = LinearRegression()

# Train the model using the sample data
model.fit(x, y)


prediction = model.predict([[9, 6, 9]])
print(prediction)
