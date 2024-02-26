import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset (replace this with your actual dataset)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Calculate covariance
covariance_matrix = df.cov()


# Plot correlation plot
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Plot of Age and Salary')
plt.show()

# Visualize the relationship between age and salary
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

print("Correlation Matrix:")
print(correlation_matrix)

print("\nCovariance Matrix:")
print(covariance_matrix)
