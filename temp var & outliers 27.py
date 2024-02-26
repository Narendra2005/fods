import pandas as pd
import numpy as np

temp=[12,5,63,2,3,64,42,33,65,32,12,34,21,45,65,31,78,89]

v=np.var(temp)
print("variance is ",v)

q1=np.percentile(temp,25)
q3=np.percentile(temp,75)
iqr=q3-q1

lb=q1-1.5*iqr
ub=q3+1.5*iqr

outliers=[]
filtered_data=[]
for x in temp:
    if x<lb or x>ub:
        outliers.append(x)
    else:
        filtered_data.append(x)

cleaned_data=[x for x in temp if x>=lb and x<=ub]

print("outliers are ",outliers)
print("filtered data ",filtered_data)
print("cleaned data",cleaned_data)
