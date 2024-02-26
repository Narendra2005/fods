import matplotlib.pyplot as plt

# Sample data for monthly temperature (replace with your actual data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [10, 12, 15, 18, 20, 22, 25, 24, 22, 18, 15, 12]
rainfall = [50, 40, 60, 55, 70, 80, 90, 100, 85, 70, 60, 45]

plt.plot(months, temperatures, marker='o', color='b', linestyle='-')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

plt.scatter(months, rainfall, color='r', marker='x')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()