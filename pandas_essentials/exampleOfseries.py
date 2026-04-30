import pandas as pd
# dictionary is made of {"key": value } so our index becomes keys

calories = {"Day1" : 2000, "Day2" : 1850, "Day3" : 2200, "Day4" : 1900,}

series = pd.Series(calories) # series is an object like creating an object through class,Series
print(series)

print(series.loc["Day2"])   #selector object > [] > access or select () > call the method

