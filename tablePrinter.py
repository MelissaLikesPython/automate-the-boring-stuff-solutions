# This program displays a list of lists of strings in a table with

# each column right-justified. 

myLists = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)    # sets the column widths
    for i in range(len(tableData)):
        tableData[i].sort(key = len)
        colWidths[i] = len(tableData[i][0]) + 4   

    for j in range(len(tableData[0])): # sets num of rows to length of first list
        for k in range(len(tableData)): # sets contents of each row
            print (tableData[k][j].rjust(colWidths[k]), end=' ')
        print()       

printTable(myLists)        
    
