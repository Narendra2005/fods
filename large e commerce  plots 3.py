import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data (replace this with your actual data)
sales_data = {
    'Product Category': ['Electronics', 'Clothing', 'Books', 'Furniture', 'Electronics', 'Clothing', 'Books', 'Furniture'],
    'Sales Amount': [5000, 7000, 3000, 4000, 6000, 8000, 3500, 4500]
}

# Create a DataFrame
df = pd.DataFrame(sales_data)

# Calculate total sales for each category
category_sales = df.groupby('Product Category')['Sales Amount'].sum()
print(category_sales)

# Line plot
plt.figure(figsize=(10, 5))
category_sales.plot(kind='line', marker='o') # sales. plot and then kind of graph is given
plt.title('Distribution of Sales Across Product Categories (Line Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(category_sales.index, category_sales.values)
plt.title('Distribution of Sales Across Product Categories (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(10, 5))
category_sales.plot(kind='bar')
plt.title('Distribution of Sales Across Product Categories (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.show()