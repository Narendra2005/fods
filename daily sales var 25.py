import numpy as np

# Sample daily sales data (replace this with your actual data)
daily_sales = [100, 110, 95, 105, 98, 102, 115, 120, 90, 105, 100, 110, 105, 100, 115, 105, 110, 100, 98, 102, 105, 100, 110, 105, 98, 102, 115, 120, 90, 105]

# Calculate the variance
variance = np.var(daily_sales)

print("Variance of daily sales:", variance)
