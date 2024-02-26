import pandas as pd

# Assuming you have a DataFrame named 'sales_data' with columns including 'CustomerID' and 'Age'
# Load your sales data into a DataFrame

# Sample DataFrame creation (replace this with your actual DataFrame)
sales_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5,6,7,8,9,10],
    'Age': [25, 30, 35, 40, 45, 50, 25, 30, 35, 40]  # Sample ages
})

# Assuming 'sales_data' contains purchase records for the past month

# Group by age and count the occurrences
age_distribution = sales_data['Age'].value_counts().sort_index()

# Print the frequency distribution
print("Age\tFrequency")
for age, freq in age_distribution.items():
    print(f"{age}\t{freq}")
