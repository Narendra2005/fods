import numpy as np

def calculate_mean_temperature(data):
    means = {}
    for city, temperatures in data.items():
        means[city] = np.mean(temperatures)
    return means

def calculate_std_deviation(data):
    std_deviations = {}
    for city, temperatures in data.items():
        std_deviations[city] = np.std(temperatures)
    return std_deviations

def calculate_temperature_range(data):
    temperature_ranges = {}
    for city, temperatures in data.items():
        temperature_ranges[city] = max(temperatures) - min(temperatures)
    return temperature_ranges

def find_most_consistent_temperature(data):
    std_deviations = calculate_std_deviation(data)
    min_std_deviation = min(std_deviations.values())
    most_consistent_cities = [city for city, std_dev in std_deviations.items() if std_dev == min_std_deviation]
    return most_consistent_cities


# Sample data containing daily temperature readings for each city over a year
data = {
        'City1': [25, 26, 24, 23, 25, 26, 27, 28, 29, 30, 30, 31, 32, 33, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24],
        'City2': [20, 21, 19, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21],
        'City3': [30, 31, 29, 28, 30, 31, 32, 33, 34, 35, 36, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25]
}

# Calculate mean temperature for each city
mean_temperatures = calculate_mean_temperature(data)
print("Mean temperatures:", mean_temperatures)
print("")
# Calculate standard deviation of temperature for each city
std_deviations = calculate_std_deviation(data)
print("Standard deviations:", std_deviations)

print("")
# Determine the city with the highest temperature range
temperature_ranges = calculate_temperature_range(data)
city_with_highest_range = max(temperature_ranges, key=temperature_ranges.get)
print("City with highest temperature range:", city_with_highest_range)

print("")
# Find the city with the most consistent temperature
most_consistent_cities = find_most_consistent_temperature(data)
print("City with most consistent temperature:", most_consistent_cities)
