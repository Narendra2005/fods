# Assuming you have the dataset in the following format
# weather_data = {'Weather Condition': ['Sunny', 'Cloudy', 'Rainy'], 'Frequency': [150, 100, 75]}

# Example dataset
weather_data = {'Weather Condition': ['Sunny', 'Cloudy', 'Rainy', 'Windy', 'Snowy'],
                'Frequency': [200, 150, 100, 80, 50]}

# Convert the dataset to a pandas DataFrame
import pandas as pd

df = pd.DataFrame(weather_data)

# Sort the DataFrame by frequency in descending order
df_sorted = df.sort_values(by='Frequency', ascending=False)

# Get the most common weather condition
most_common_weather = df_sorted.iloc[0]['Weather Condition']
frequency_of_most_common = df_sorted.iloc[0]['Frequency']

# Print the most common weather condition and its frequency
print("Most common weather condition:", most_common_weather)
print("Frequency:", frequency_of_most_common)

# Print the frequency distribution
print("\nFrequency Distribution:")
print(df_sorted)
