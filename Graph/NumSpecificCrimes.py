from Analyser import *

mainDF = separate("./Crime_data.csv")

numCrimesPerType = sumColumn(mainDF, "Crm Cd Desc", False, excess=None)

typesDF = dictToDF(numCrimesPerType, "Crime Type", "Num Crimes")

plotBarGraph(typesDF, "Crime Type", "Num Crimes", "Type of Crime", "Number of Crimes")