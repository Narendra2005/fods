import numpy as np

# Assuming you have a NumPy array named fuel_efficiency containing fuel efficiency data

fuel_efficiency = np.array([25, 30, 28, 32, 27, 24, 29, 31, 26])


average_fuel_efficiency = np.mean(fuel_efficiency)

# 2. Determine the fuel efficiency of the two specific car models

model1_efficiency = fuel_efficiency[2]
model2_efficiency = fuel_efficiency[5]

# 3. Calculate the percentage improvement in fuel efficiency between the two car models
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100

# Print the results
print("Average fuel efficiency:", average_fuel_efficiency)
print("Fuel efficiency of Model 1:", model1_efficiency)
print("Fuel efficiency of Model 2:", model2_efficiency)
print("Percentage improvement in fuel efficiency:", percentage_improvement, "%")
