import pandas as pd
# csv means = comma-separated values
# json means = javascript object notation >> shortened [{"key": "value"}]

df = pd.read_csv("data.csv")
print(df.to_string()) # it helps us to write all values from 0 to the end 

df1 = pd.read_json("data.json")
print(df1)
print(df1.loc[0])