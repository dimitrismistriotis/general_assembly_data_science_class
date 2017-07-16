import pandas as pd

df = pd.DataFrame({
  "Person": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "Mood Score": [2, 6, 7, 10, 4, 2, 3, 5, 5, 7]})

sum1 = sum(df[df["Person"] >= 2]["Mood Score"]**3)
print(sum1)

sum2 = sum(df[(df["Person"] >= 2)&(df["Person"] <= 9)]["Mood Score"]**2)
print(sum2)
