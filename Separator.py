import pandas

pandas.set_option('display.max_columns', None)
df = pandas.read_csv("Crime_data.csv")

df.drop([
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



### Date stuff
df["DATE OCC"] = pandas.to_datetime(df["DATE OCC"])

datesList = list(df["DATE OCC"])
numCrimesPerDate = {}
for i in datesList:
    try:
        numCrimesPerDate[str(i)[:-9]] += 1
    except KeyError:
        numCrimesPerDate[str(i)[:-9]] = 1

print(numCrimesPerDate)


datesDFDict = {}
datesDFDict["DATE"] = numCrimesPerDate.keys()
datesDFDict["Num Crimes"] = [numCrimesPerDate[i] for i in numCrimesPerDate.keys()]

datesDF = pandas.DataFrame(datesDFDict)

print(datesDF)



