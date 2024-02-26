import matplotlib.pyplot as plt

# Sample data
values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# Create a box plot
plt.figure(figsize=(8, 6))
#plt.boxplot(values, patch_artist=True, boxprops=dict(facecolor='orange'))
plt.boxplot(values)
plt.title('Box Plot of Sample Values')
plt.xlabel('Data')
plt.ylabel('Values')
plt.grid(True)
plt.show()


import numpy as np

# List of months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Number of days in each month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Calculate number of days between each month
days_between_months = np.diff(days_in_month)

# Print the number of days between each month
for i in range(len(months) - 1):
    print(f"Number of days between {months[i]} and {months[i+1]}: {days_between_months[i]}")
