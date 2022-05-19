# Duplicate Finder

This will find duplicates in a single column of a csv

## How to Use

1. Install Python3 https://flaviocopes.com/python-installation-macos/
2. Download this repo (click the green code button at the top right and then download zip).
3. Save your csv data file in the same folder as this repo.
4. Open a terminal window and navigate to the folder where you saved. Right click on the finder window and click services and then click New Termianl at Folder
5. Once in the directory run the followng command from the terminal window:

``python3 ./dupChecker.py {your_filename.csv} {column_name}``

 {column_name} is optional. If it is excluded, the first column in the csv will be checked for duplicates

## Examples
``python3 ./dupChecker.py input.csv state``

``python3 ./dupChecker.py input.csv``

``python3 ./dupChecker.py dup_emails_may_2.csv email``

``python3 ./dupChecker.py dup_emails_may_2.csv "subscription id"``

### Explanation of the command
``python3`` indicates that you will be executing a python script

``./dupChecker.py`` indicates that the python script you are executing is in the current directory (./) and its name is "dupChecker.py"

``input.csv`` or ``dup_emails_may_2.csv`` are names of input files. Replace these with whatever name your data file has. It is recommended to use a filename without spaces or special characters in it.

``state`` or ``email`` or ``subscription id`` is optional and is the name of the column of your data file that you want to check duplicates on. If the column name has a space in it like "subscription id" put the name in double quotes like it is above.

## Output you will see

The program produces output in 3 places:

### summary.txt

Summary.txt is a text file with the count of duplicates and the duplicate data with any rows listed where the duplicates occur.

### duplicates.csv

All of the duplicates are listed here and essentially extracted from your original file. They will be grouped by the column name you provided.

### console output

You should see the same output from summary.txt in the terminal window as well.


# Tutorial

View this loom video for help if you are from Word on Fire.

https://www.loom.com/share/50f63a0cabf24e65ac29335b476adb8c 