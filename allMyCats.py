# This programme is for adding cats to a list.

catNames = []
while True:
    print('Enter the name of cat number ' + str(len(catNames) + 1) +
          ' (or simply press \'Enter\' to finish).')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # Concatenation of cats to the list.
print('The names of the cats are:')
for name in catNames:
    print(' ' + name)
          

