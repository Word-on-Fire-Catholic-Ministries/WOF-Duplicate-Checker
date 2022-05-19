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
#Take filename from command line.
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

duplicateOccurenceCount = {} # = pieceOfData => int
duplicateRowNumbers = {} # pieceOfData => [int, int, int]
duplicateRows = {} # pieceOfData => [row, row, row]

duplicatesFound = 0

headerArray = []

with open(filename) as input:
    csvReader = csv.reader(input)
    columnToCheck = 0 # what column of the csv to check for duplicates
    currentRowNumber = 0 # loop incrementer
    for row in csvReader:        
        if(currentRowNumber == 0 and columnNameToCheck != ''):
            columnToCheck = verifyFirstColumnExists(row, columnNameToCheck)
            currentRowNumber = currentRowNumber + 1
            headerArray = row #store this when writing output out later
            continue

        if(row[columnToCheck] in duplicateOccurenceCount): #duplicate found
            duplicateOccurenceCount[row[columnToCheck]] = duplicateOccurenceCount[row[columnToCheck]] + 1
            duplicateRowNumbers[row[columnToCheck]].append(currentRowNumber)
            duplicateRows[row[columnToCheck]].append(row)
            duplicatesFound = duplicatesFound + 1
        
        else: # Not a duplicate
            duplicateOccurenceCount[row[columnToCheck]] =  1
            duplicateRowNumbers[row[columnToCheck]] = [currentRowNumber]
            duplicateRows[row[columnToCheck]] = [row]
        
        currentRowNumber = currentRowNumber + 1
input.close()

print(str(duplicatesFound) + " duplicates found")

for key in duplicateRowNumbers:
    if(len(duplicateRowNumbers[key]) > 1):
        print(key + " is a duplicate among " + str(duplicateOccurenceCount[key]) + " rows ")
        for rowNum in duplicateRowNumbers[key]:
            print(str(rowNum))

###
# Write Summary to a txt file
###
with open('./summary.txt', 'w') as output:
    output.write("Checked "+filename + " for duplicates\n")
    output.write(str(duplicatesFound) + " duplicates found\n")
    for key in duplicateRowNumbers:
        if(len(duplicateRowNumbers[key]) > 1):
            output.write(key + " is a duplicate among " + str(duplicateOccurenceCount[key]) + " rows \n")
            for rowNum in duplicateRowNumbers[key]:
                output.write("\trow "+str(rowNum)+"\n")

output.close()

###
# Write Duplicates to a csv file
###
with open('./duplicates.csv', 'w') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(headerArray)
    for key in duplicateRows:
        if(len(duplicateRows[key]) > 1):
            for row in duplicateRows[key]:
                writer.writerow(row)

output_csv.close()