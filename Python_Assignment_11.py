import pandas as pd
import numpy as np

#Create a sries containing 10 random numbers
s = pd.Series(np.random.randint(1,100,10))

print("Series")
print(s)

#Indexing
print("\n Element at index 3:", s[3])

#Filtering
print("\n Number greater than 50")
print(s[s>50])

# Statistical operations

print("\nMean",s.mean())
print("median",s.median())
print("minimum",s.min())
print("maximum",s.max())
