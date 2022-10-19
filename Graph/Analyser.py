import pandas
import matplotlib.pyplot as plt

pandas.set_option('display.max_columns', None)

# preprocesses the data
def separate(df_string):
    df = pandas.read_csv(df_string)

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
    
    return df

# sums the number of entries that satisfy a requirement in a column i.e amount of crimes per date
def sumColumn(df, column, sorted_=False, excess=None):

    columnList = sorted(list(df[column])) if sorted_ else list(df[column])
    numYPerX = {}
    for i in columnList:
        try:
            numYPerX[str(i)[:excess]] += 1
        except KeyError:
            numYPerX[str(i)[:excess]] = 1
    
    return numYPerX

# converts the dictionary returned from the sumcolumn function into a pandas dataframe
def dictToDF(mainDict, X, Y):
    dfDict = {}
    dfDict[X] = mainDict.keys()
    dfDict[Y] = [mainDict[i] for i in mainDict.keys()]
    dataFrame = pandas.DataFrame(dfDict)

    return dataFrame

# plots a line graph
def plotLineGraph(df, y, xlabel, ylabel):
    plt.plot(df[y], marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation='vertical', fontsize = 8)
    plt.show()

#plots a bar graph
def plotBarGraph(df, x, y, xlabel, ylabel):
    plt.bar(df[x], df[y])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation='vertical', fontsize = 4)
    plt.show()


# only runs the example if entire file is run
# doesnt run the example if entire file is imported into one of the graphing files
if __name__ == "__main__":

    ## Example

    # preprocesses dataset
    mainDF = separate("./Crime_data.csv")

    # converts DATE_OCC to a datetime object
    mainDF["DATE OCC"] = pandas.to_datetime(mainDF["DATE OCC"])

    # sums a column(finds all the crimes that occured on each date and adds the counts together)
    # df is the dataset, DATE_OCC is the date occurred, sorted_ is an option for sorting before summing(for time series')
    # and excess is for eliminating excess values from the end of each string
    numCrimesPerDate = sumColumn(mainDF, "DATE OCC", sorted_=True, excess=-9)

    # converts the dictionary of the number of crimes per date into a pandas dataframe
    datesDF = dictToDF(numCrimesPerDate, "DATE", "Num Crimes")

    ## Post Processing for unique data evaluations
    # converts a column of strings into a column of type datetime64 and sets the column as the index
    datesDF["DATE"] = datesDF["DATE"].astype("datetime64")
    datesDF = datesDF.set_index("DATE")

    # plots a line graph
    plotLineGraph(datesDF, "Num Crimes", "Date", "Number of Crimes")