import pandas as pd

d={"quater":["q1","q2","q3","q4"],
   "sales": [25000,30000,35000,40000]}

df=pd.DataFrame(d)

tsales=df["sales"].sum()
print("total sales  ",tsales)

percent_inc=((df["sales"][3]-df["sales"][0])/df["sales"][0])*100
print("percentile increase from q1 to q4 is ", percent_inc)

