# Duplicate Finder

This will find duplicates in a single column of a csv

## How to Use

1. Install Python3 https://flaviocopes.com/python-installation-macos/
2. Download this repo (click the green code button at the top right and then download zip).
3. Save your csv data file in the same folder as this repo.
4. Open a terminal window and navigate to the directory where you saved this repo using cd.
5. Once in the directory run the followng command
``python3 ./dupChecker.py {your_filename.csv} {column_name}``
 {column_name} is optional. If it is excluded, the first column in the csv will be checked for duplicates

## Examples
``python3 ./dupChecker.py input.csv state``

``python3 ./dupChecker.py input.csv``

``python3 ./dupChecker.py dup_emails_may_2.csv email``

## Output you will see

The program produces output in 3 places:

### summary.txt

Summary.txt is a text file with the count of duplicates and the duplicate data with any rows listed where the duplicates occur.

### duplicates.csv

All of the duplicates are listed here and essentially extracted from your original file. They will be grouped by the column name you provided.

### console output

You should see the same output from summary.txt in the terminal window as well.