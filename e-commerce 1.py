
import pandas as pd
d={"oid":[101,102,102,304,102], "cid":[1,2,1,3,2],"pid":[12,12,34,12,23],"qnty":[1,2,4,5,6],"tprice":[342,454,651,898,999]}

df=pd.DataFrame(d)
df.head()

totprice=sum(df["tprice"])
print(totprice)

avgqnty=df["qnty"].mean()
print(avgqnty)

top_pdt=df.groupby("pid")["qnty"].sum()
print(top_pdt)
