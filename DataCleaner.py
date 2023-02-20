import csv
import matplotlib.pyplot as plt

def fileOpen(fileName, column):
    """Function to extract data from a .csv file
    fileName - name of file
    index - column index to be extracted"""
    # Open the .csv file for data extraction
    with open(fileName) as file:
        fileData = csv.reader(file)
        # Create a new list to write each entry to
        fileList = []
        # Skip the first (title) line
        next(fileData)
        # Iterate through file, writing each entry to the data list as a float
        for term in fileData:
            fileList.append(float(term[column]))
        return(fileList)
    
def plotData(x, y, title):
    """Function to plot a graph of x against y
    # x - data to be mapped to the x-axis - in this case, years
    # y - data to be mapped to the y-axis - in this case, area
    # title - title to be written above the graph"""
    # Create the graph to be output
    plt.plot(x, y)
    # Lock y-axis to origin
    plt.ticklabel_format(useOffset=False)
    # Label x- and y- axes
    plt.xlabel('Year')
    plt.ylabel('Area above sea level (km\N{SUPERSCRIPT TWO})')
    # Write title of graph
    plt.title(title)
    # Save graph as a pdf
    plt.savefig(title + ".pdf")
    # Display graph and close the function so new data is mapped to a new graph
    plt.show()

def dataClean(dataList :list):
    startCounter = -1
    outputList = []
    xList = []
    for currentCounter in range(0, len(dataList)):
#        print(dataList[currentCounter])
        if dataList[currentCounter] < 0:
            divisor = currentCounter-(startCounter+1)
            for index in range(startCounter+1, currentCounter):
                outputList[index] = dataList[index] + (dataList[currentCounter] / divisor)
            outputList.append(0.0001)
            startCounter = currentCounter
        else:
            outputList.append(dataList[currentCounter])
    xList.append(currentCounter)
    return outputList, xList

fileN = "Data1.csv"

dataset = fileOpen(fileN, 0)
dataPostClean, xValues = dataClean(dataset)

Count = 2

for term in dataPostClean:
#    print(str(Count) + " " + str(term))
    print(term)
    Count += 1

# Nominal change
# Another arbitrary change
# Owen tries to fix the code

# Jack ruins the code

#breaking the code

for i in range(0, 10):
    print(i)


    # Owen ruins is shit at coding