import pandas as pd
import math as math

df = pd.DataFrame({"Price": [10, 10, 10, 15, 15, 15, 20, 20, 20, 25, 25, 25],
  "Design": [0, 5, 10, 0, 5, 10, 0, 5, 10, 0, 5, 10]})

df['Sales'] = 20.0 + (df['Design']**2 / (df['Price'] + 10.0)**0.5)

print(df)
