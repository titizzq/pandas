import pandas as pd

data = {"Name": ["Spongebob","Patrick","Squidward"], # these are columns
        "Age": [19,25,30],
        "Position": ["cook", "intern","Manager"]}

df = pd.DataFrame(data,index=["employee1","employee2","employee3"]) # index is our rows

print(df)
print(df.loc["employee1"])
print(df.iloc[1])

print("----------------------------------")

# Adding a new column

df["Height"]= [150,165,170]
print(df)
print("---------------------------------")

# Adding a new row

new_row = pd.DataFrame([{"Name": "Crab", "Age": 43,"Position": "N/A","Height": 175}],index=["employee4"])

df = pd.concat([df,new_row])
print(df)