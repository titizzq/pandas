import pandas as pd

df = pd.read_csv("data.csv")

# filtering = keeping the rows that match a condition

#tall_pokemon = df[df["Height"]>2]
#legendary_ones = df[df["Legendary"] == 1]
ice_flying_ones = df[(df["Type1"] == "Ice") & (df["Type2"] == "Flying")]  # df[ (condition) | (condition2) ]

print(ice_flying_ones)