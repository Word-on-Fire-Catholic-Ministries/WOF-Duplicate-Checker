###
# Takes a csv file as input and a column name and checks for duplicate values 
### in that column

import sys, csv

###
# Take a csv header array and return the index of the given 
# column name in that array
###
def verifyFirstColumnExists(csvHeader, columnName):
    columnIndex = 0
    for heading in csvHeader:
        if heading == columnName:
            return columnIndex
        columnIndex = columnIndex + 1
    exit("Column name '"+columnName + "' is not in the top row of the csv. Try again.")

###
#Take filename from command line. If no arg, use 'input.csv'
###
filename = ''
if(len(sys.argv) < 2):
    exit("No file name provided.")
else:
    filename = sys.argv[1]
    print("Checking "+filename + " for duplicates...")

###
#Take the column name from the command line. If no arg, use the first column
###
columnNameToCheck = ''
if(len(sys.argv) >= 3):
    columnNameToCheck = sys.argv[2]

duplicateOccurenceCount = {} # = pieceOfData => frequency
duplicateRows = {} # pieceOfData => [row, row, row]

duplicatesFound = 0

with open(filename) as input:
    csvReader = csv.reader(input)
    columnToCheck = 0 # what column of the csv to check for duplicates
    currentRowNumber = 0 # loop incrementer
    for row in csvReader:        
        if(currentRowNumber == 0 and columnNameToCheck != ''):
            columnToCheck = verifyFirstColumnExists(row, columnNameToCheck)
            currentRowNumber = currentRowNumber + 1
            continue

        if(row[columnToCheck] in duplicateOccurenceCount):
            duplicateOccurenceCount[row[columnToCheck]] = duplicateOccurenceCount[row[columnToCheck]] + 1
            duplicateRows[row[columnToCheck]].append(currentRowNumber)
            duplicatesFound = duplicatesFound + 1
        else:
            duplicateOccurenceCount[row[columnToCheck]] =  1
            duplicateRows[row[columnToCheck]] = [currentRowNumber]
        
        currentRowNumber = currentRowNumber + 1
input.close()

print(str(duplicatesFound) + " duplicates found")

for key in duplicateRows:
    if(len(duplicateRows[key]) > 1):
        print(key + " is a duplicate among " + str(duplicateOccurenceCount[key]) + " rows ")
        for rowNum in duplicateRows[key]:
            print("\trow "+str(rowNum))

###
# Write Output
with open('./output.csv', 'w') as output:
    output.write("Checking "+filename + " for duplicates...\n")
    output.write(str(duplicatesFound) + " duplicates found\n")
    for key in duplicateRows:
        if(len(duplicateRows[key]) > 1):
            output.write(key + " is a duplicate among " + str(duplicateOccurenceCount[key]) + " rows \n")
            for rowNum in duplicateRows[key]:
                output.write("\trow "+str(rowNum)+"\n")

output.close()



