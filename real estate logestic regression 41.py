import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Step 1: Create a default dictionary with 15 values and the mentioned attributes
data = {
    'house_size': [1200, 1500, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3500, 3800, 4000, 4200, 4500],
    'num_bedrooms': [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7],
    'location': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C'],
    'house_age': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'house_price': [300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000]
}

# Step 2: Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Perform bivariate analysis
selected_feature = 'house_size'
target_variable = 'house_price'

# Plotting the bivariate analysis
import matplotlib.pyplot as plt
plt.scatter(df[selected_feature], df[target_variable])
plt.title('Bivariate Analysis: House Size vs House Price')
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.show()

# Step 4: Build a linear regression model
X = df[selected_feature]
y = df[target_variable]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model's performance
y_pred = model.predict(X_test)

# Calculating evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Printing evaluation metrics
print(f'Mean Squared Error (MSE): {mse}')
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Root Mean Squared Error (RMSE): {rmse}')
print(f'R-squared (R2): {r2}')
