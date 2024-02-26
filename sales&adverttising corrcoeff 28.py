import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
sales = [100, 120, 130, 145, 160, 180, 200, 210, 230, 250, 270, 280]
advertising = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(sales, advertising)[0, 1]

# Create scatter plot
plt.scatter(advertising, sales, color='blue')
plt.title('Sales vs Advertising')
plt.xlabel('Advertising spent')
plt.ylabel('Number of sales')
plt.grid(True)
plt.show()

print("Correlation Coefficient:", correlation_coefficient)
