import pandas

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("Crime_data.csv")

df.drop(["DR_NO", "AREA", "Rpt Dist No"], axis=1, inplace=True)

print(df)
