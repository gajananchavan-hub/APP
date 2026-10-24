

import numpy as np
import pandas as pd

prices = np.array([450, 600, 350, 750, 500, 900])

average = np.mean(prices)

df = pd.DataFrame({
    "Book Price": prices
})

print("Book Prices:")
print(df)

print("\nAverage Book Price:", average)

print("\nBooks costing more than ₹500:")
print(df[df["Book Price"] > 500])

import numpy as np
import pandas as pd

prices = np.array([450, 600, 350, 750, 500, 900])

average = np.mean(prices)

df = pd.DataFrame({
    "Book Price": prices
})

print("Book Prices:")
print(df)

print("\nAverage Book Price:", average)

print("\nBooks costing more than ₹500:")
print(df[df["Book Price"] > 500])
