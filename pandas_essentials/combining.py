import pandas as pd

df = pd.read_csv("data.csv")

# aggregate functions >> Reduces a set of values into a single summary value
# Used to summarize and analyze data
# Often used with the groupby) function



# whole dataframe
# print(df.mean(numeric_only=True)) # it gives us average values of all data,the reason why we use numeric_only just because we have columns that are not numeric for example the names of all pokemons
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count()) # just counting how many values there are


# single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())

# groupby
group = df.groupby("Type1") # we are taking pokemons who have in common attribute(Type 1) and we are grouping them into the another groups like fire groups or ice groups
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
