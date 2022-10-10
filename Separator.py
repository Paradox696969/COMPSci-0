import pandas

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("Crime_data.csv")

df.drop([
        "DR_NO",
        "AREA",
        "Rpt Dist No", 
        "Part 1-2", 
        "Crm Cd", 
        "Mocodes", 
        "Premis Cd" , 
        "Weapon Used Cd" , 
        "Status" , 
        "Status Desc" , 
        "Crm Cd 1",
        "Crm Cd 2",
        "Crm Cd 3",
        "Crm Cd 4",
        "LOCATION",
        "Cross Street",
        "LAT",
        "LON"
        ], 
        axis=1, inplace=True)


print(df)
