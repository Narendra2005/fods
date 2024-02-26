import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Creating a default dictionary
data = {
    'CustomerID': np.random.randint(1000, 2000, 15),
    'AmountSpent': np.random.randint(50, 500, 15),
    'Frequency': np.random.randint(1, 20, 15)
}

# Converting the dictionary into a DataFrame
df = pd.DataFrame(data)
print(df)

# Scaling the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['AmountSpent', 'Frequency']])

# Creating a DataFrame with scaled features
scaled_df = pd.DataFrame(scaled_features, columns=['AmountSpent', 'Frequency'])
print(scaled_df)

# Building the K-Means clustering model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_df)

# Assigning clusters to the original DataFrame
df['Cluster'] = kmeans.labels_

print(df)

