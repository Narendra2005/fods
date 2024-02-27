import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Define the default dictionary
data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015],
    'Age': [25, 35, 45, 30, 28, 40, 55, 32, 34, 44, 48, 29, 38, 50, 60],
    'Income': [50000, 60000, 75000, 90000, 70000, 80000, 95000, 110000, 100000, 120000, 130000, 105000, 115000, 125000, 140000],
    'SpendingScore': [75, 60, 45, 80, 85, 70, 30, 75, 80, 60, 55, 90, 50, 20, 15]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Preprocessing: Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop('CustomerID', axis=1))

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(df['Income'], df['SpendingScore'], c=df['Cluster'], cmap='viridis')
plt.title('Customer Segmentation')
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.show()

# Output the clusters
print(df)
