'''
Takes a csv file as input and a column name and checks for duplicate values 
in that column
'''

import sys

'''
Take filename from command line. If no arg, use 'input.csv'
'''
n = len(sys.argv)
filename = ''
if(n < 2):
    filename = 'input.csv'
    print("No file name provided. Will check input.csv")
else:
    filename = sys.argv[1]
    print("Will check "+filename)
