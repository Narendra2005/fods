import pandas as pd

# Creating a default DataFrame
data = {
    'Server_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Response_Time': [100, 120, 150, 180, 200, 210, 230, 250, 280, 300],
    'CPU_Utilization': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Memory_Utilization': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
}

df = pd.DataFrame(data)

# Calculating percentiles
percentiles = df['Response_Time'].quantile([0.25, 0.5, 0.75])
print(percentiles)

# Displaying the percentiles
print("25th Percentile:", percentiles[0.25])
print("50th Percentile (Median):", percentiles[0.5])
print("75th Percentile:", percentiles[0.75])

