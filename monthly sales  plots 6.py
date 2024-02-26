import pandas as pd
d={"mon":["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"],
"sales":[1000,2312,3289,5432,1273,8231,3498,7347,3479,7532,3480,1830]}

df=pd.DataFrame(d)
print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
plt.plot(df["mon"], df["sales"], marker='o', color='red', linestyle='-')
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

plt.figure(figsize=(5,5))
plt.bar(df["mon"],df["sales"],color="skyblue")
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Show gridlines on y-axis only
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
