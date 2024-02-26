import pandas as pd

sales=pd.DataFrame({
    "pdt":["pdt A","pdt B","pdt A","pdt C","pdt D","pdt E","pdt D","pdt F","pdt B","pdt C"],
    "qnty":[123,431,472,873,238,326,998,362,121,643]
})

groupeddf=sales.groupby("pdt")["qnty"].sum()
print(groupeddf)

top_pdts=groupeddf.sort_values(ascending=False)
print(top_pdts.head())