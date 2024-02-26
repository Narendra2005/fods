import pandas as pd
d={"mon":["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"],
"sales":[1000,2312,3289,5432,1273,8231,3498,7347,3479,7532,3480,1830]}

df=pd.DataFrame(d)
print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df["mon"], df["sales"], marker='o', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["mon"], df["sales"], color='blue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df["mon"], df["sales"], color='green')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y')  # Show gridlines on y-axis only
plt.show()
