from Analyser import *

df = pandas.read_csv("Inflation-Estimated.csv")
df["Date"] = df["Date"].astype("datetime64")
df = df.set_index("Date")
plotLineGraph(df, "Rate", "Date", "Rate of Inflation")