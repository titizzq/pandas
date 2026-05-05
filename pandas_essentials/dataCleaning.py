import pandas as pd

df  = pd.read_csv("data.csv")

# 1. Drop irrelevant columns

# df = df.drop(columns=["Type1", "Type2"])
# print(df)

# 2. Handle missing data

# df = df.dropna(subset = ["Type2"]) # dropna means drop not avaliable > NaN > Not a number
# df = df.fillna({"Type2":"None"}) # fill not avaliable we filled the not avaliable key values to None word could be anything

# 3. Fix inconsistent values

# df["Type1"] = df["Type1"].replace({"Grass":"GRASS"}) # that dictionary tells you "old value " : "new value " its different than key value but still works same

# 4. Standardize Text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. Fix Data Types
# df["Legendary"] = df["Legendary"].astype(bool) # astype means change the type as a boolean
# print(df.to_string())

# 6. Remove Duplicate values
# df = df.drop_duplicates()
# print(df.to_string())
