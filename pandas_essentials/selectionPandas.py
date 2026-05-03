import pandas as pd

#df = pd.read_csv("data.csv")
#print(df.to_string())


# Selection by column

#print(df["Type1"].to_string()) # it gives you a series

#print(df[["Name","Height"]]) # Pandas requires a python list to select multiple columns. it gives you a dataframe, inner brackets are a list and other brackets are subscript



# Selection by row

df = pd.read_csv("data.csv", index_col="Name") # our label becomes index column > Name

print(df.loc["Pikachu",["Height","Weight"]])

print(df.loc["Pikachu":"Ninetales"]) # give me the values between pikachu and ninetales

print(df.iloc[0:5,0:3]) # 0:3 means give me the first three columns





