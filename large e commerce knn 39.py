import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Creating a default dictionary
data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015],
    'TotalAmountSpent': [200, 350, 400, 600, 100, 800, 150, 2000, 250, 300, 500, 700, 800, 1000, 1200],
    'NumItemsPurchased': [4, 3, 5, 6, 2, 7, 3, 10, 2, 3, 5, 6, 7, 8, 9]
}

# Converting dictionary to DataFrame
df = pd.DataFrame(data)

# Normalizing the data
df_normalized = (df - df.mean()) / df.std()

# Applying K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df_normalized[['TotalAmountSpent', 'NumItemsPurchased']])
df['Cluster'] = kmeans.labels_

# Visualizing the clusters
plt.figure(figsize=(10, 6))
plt.scatter(
    df['TotalAmountSpent'],  # X-axis data: Total amount spent by customers
    df['NumItemsPurchased'],  # Y-axis data: Number of items purchased by customers
    c=df['Cluster'],  # Color of each point determined by the cluster assigned to the corresponding data point
    cmap='viridis',  # Colormap to be used for coloring points (viridis is a predefined colormap in matplotlib)
    edgecolors='k',  # Color of the edges of markers (in this case, black)
    alpha=0.7  # Transparency of markers (0 being completely transparent and 1 being completely opaque)
)

plt.title('K-Means Clustering of Customer Purchasing Behavior')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()
