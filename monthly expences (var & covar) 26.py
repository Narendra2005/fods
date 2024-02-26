import pandas as pd
import numpy as np
data={
    "dept1":[10000, 12000, 11000, 9000],
    "dept2":[8000, 9000, 8500, 9500],
    "dept3":[12000, 11000, 10000, 10500],
    "dept4":[9500, 9800, 9300, 9100]
}


df=pd.DataFrame(data)
print(np.var(df["dept3"]))
var_l={}
for dep,l in df.items():
    var_l[dep]=df[dep].var()


print("variance is ",var_l)
print("covariance ")
covar=np.cov(df)
for r in covar:
    print(r)

