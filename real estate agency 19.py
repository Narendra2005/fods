import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
    'bedrooms': [3, 2, 4, 5, 2],
    'area_sqft': [2000, 1500, 2400, 1800, 1700],
    'listing_price': [300000, 250000, 400000, 320000, 270000],
}

df=pd.DataFrame(data)

#The average listing price of properties in each location.
d=df.groupby("location")["listing_price"].mean()
print(d)

#The number of properties with more than four bedrooms.
d=df[df["bedrooms"]>4]
print(d)
print("no of properties with more than 4 bed rooms ",len(d))

#The property with the largest area.
print("property with largest area ",df["area_sqft"].max())