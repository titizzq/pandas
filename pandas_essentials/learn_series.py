import pandas as pd

data = [100,200,300,400]

series = pd.Series(data,index=["a","b","c","d"])

print(series.loc["b"]) # loc means location by label and our labels are our index a,b,c,d for example
print(series.iloc[0])  # iloc means integer location like index 0,1,2 like accessing a value in array

series.loc["c"] = 305 # we are also accessing our label and give a new variable

print(series)
print(series[series >= 200])

