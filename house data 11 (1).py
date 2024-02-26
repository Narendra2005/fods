import pandas as pd

df=pd.read_csv("housedata.csv")

print(df.head())
# Filter houses with more than four bedrooms
ndata=df[df["bedroomno"]>4]
print(ndata)
avg_price=ndata["salesprice"].mean()
print("avg sales price is ",avg_price)
