import collections
reviews = [
    "This product is great!",
    "I love this product",
    "Best purchase ever",
    "This is a great product",
    "I am so happy with this product"
]

joined=" ".join(reviews)
list=joined.split()
d={}
for i in list:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)