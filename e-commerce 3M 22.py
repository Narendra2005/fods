import pandas as pd

# Default DataFrame with purchase amounts
data = {
    'Transaction_ID': [101, 102, 103, 104, 105],
    'Purchase_Amount': [50, 40, 50, 60, 70],
    'Customer_ID': [1, 2, 3, 4, 5],
    'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Grocery', 'Electronics']
}

df = pd.DataFrame(data)

# Calculate the mean (average) purchase amount
mean_purchase_amount = df['Purchase_Amount'].mean()

median_purchase_amount = df['Purchase_Amount'].median()

# Identify the mode of purchase amounts
mode_purchase_amount = df['Purchase_Amount'].mode()

print("Mean (average) purchase amount: $", round(mean_purchase_amount, 2))
print("Median of purchase amounts:", median_purchase_amount)
print("Mode of purchase amounts:", mode_purchase_amount[0])
