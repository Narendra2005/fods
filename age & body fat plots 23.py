import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create a DataFrame with age and %fat data
data = {
    'Age': [25, 35, 45, 55, 65, 25, 35, 45, 55, 65, 25, 35, 45, 55, 65, 25, 36, 47],
    'Fat': [18.2, 25.4, 30.2, 28.5, 20.3, 22.6, 26.2, 30.9, 27.8, 21.9, 19.2, 28.5, 31.3, 29.7, 23.8, 20.4, 24.5, 26.1]
}

df = pd.DataFrame(data)

print("age mean ",df["Age"].mean())
print("age median",df["Age"].median())
print("age mode ",df["Age"].mode()[0])
print("age st dev ",df["Age"].std())

print("fat mean ",df["Fat"].mean())
print("fat median",df["Fat"].median())
print("fat mode ",df["Fat"].mode()[0])
print("fat st dev ",df["Fat"].std())

#box plots

plt.figure(figsize=(4,4))
plt.boxplot(df["Age"])
plt.title("box plot of age ")
plt.show()

plt.figure(figsize=(4,4))
plt.boxplot(df["Fat"])
plt.title("box plot of fat ")
plt.show()

plt.figure(figsize=(5,5))
plt.scatter(df["Age"],df["Fat"])
plt.title("scatter plot of age vs fat ")
plt.xlabel("age")
plt.ylabel("fat")
plt.grid(True)
plt.show()

# Creating Q-Q plot
plt.figure(figsize=(8, 6))
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
stats.probplot(df['Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of %Fat')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.show()
