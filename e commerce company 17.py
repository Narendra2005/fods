import pandas as pd
data = {
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2023-07-31', '2023-07-30', '2023-07-29', '2023-07-30', '2023-07-31', '2023-07-28'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'order_quantity': [3, 2, 1, 4, 3, 2]
}

df=pd.DataFrame(data)

orderpercust=df.groupby("customer_id")["product_name"].count()
print(orderpercust)

avg_qnty=df.groupby("product_name")["order_quantity"].mean()
print(avg_qnty)

print("early order date ",df["order_date"].min())
print("early order date ",df["order_date"].max())

