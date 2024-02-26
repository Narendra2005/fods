import pandas as pd

# Creating a sample DataFrame with recovery time data
data = {
    'Patient_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Recovery_Time (days)': [3, 5, 6, 7, 8, 9, 10, 12, 14, 18]
}

df = pd.DataFrame(data)

# Calculate percentiles
percentiles = df['Recovery_Time (days)'].quantile([0.1, 0.5, 0.9])

# Display the percentiles
print("10th Percentile (0.1 quantile):", percentiles[0.1])
print("50th Percentile (Median, 0.5 quantile):", percentiles[0.5])
print("90th Percentile (0.9 quantile):", percentiles[0.9])
