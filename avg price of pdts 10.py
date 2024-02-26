import numpy as np
# Assuming sales_data is a NumPy array where each row represents the sales for a different product
data =np.array([
    [10.50, 15.25, 20.00],  # Product 1 sales (price per unit)
    [8.75, 12.00, 18.50],   # Product 2 sales
    [14.00, 17.50, 21.75]
])

avg_per_pdt=np.mean(data,axis=1)
print(avg_per_pdt)

for i,avg_pdt in enumerate(avg_per_pdt):
    print(f"product {i+1} avg is { avg_pdt}")