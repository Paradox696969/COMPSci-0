from Analyser import *

mainDF = separate("./Assets/Crime_data.csv")
mainDF["DATE OCC"] = pandas.to_datetime(mainDF["DATE OCC"])

numCrimesPerDate = sumColumn(mainDF, "DATE OCC", sorted_=True, excess=-9)
numCrimesPerType = sumColumn(mainDF, "Crm Cd Desc", False, excess=None)

df1 = dictToDF(numCrimesPerDate, "DATE", "Num Crimes")
df2 = dictToDF(numCrimesPerType, "Crime Type", "Num Crimes")
infdf = pandas.read_csv("Inflation-Estimated.csv")

outDict = {"GraphType": ["Crimes per Date", "Crimes by Type", "Inflation Rate"], 
            "Mean": [mean(list(df1["Num Crimes"])), mean(list(df2["Num Crimes"])), mean(list(infdf["Rate"]))],
            "Median": [median(list(df1["Num Crimes"])), median(list(df2["Num Crimes"])), median(list(infdf["Rate"]))],
            "Mode": [mode(list(df1["Num Crimes"])), mode(list(df2["Num Crimes"])), mode(list(infdf["Rate"]))],
            "Range": [rangeStat(list(df1["Num Crimes"])), rangeStat(list(df2["Num Crimes"])), rangeStat(list(infdf["Rate"]))]
            
        }

outDf = pandas.DataFrame(outDict)
print(outDf)

