myList = ['rabbit', 'cat', 'horse', 'housemartin', 'fox']              

def commaCode(myList):
    for i in range(len(myList) - 1):
        print(myList[i] + ', ', end='')
    print('and ' + myList[-1], end='')
    
commaCode(myList)    
