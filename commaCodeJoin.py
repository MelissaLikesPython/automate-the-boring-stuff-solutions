# Use .join to concatenate string items in a list.

spam = ['apples', 'bananas', 'tofu', 'cats']

print(', '.join(spam[0:-1]), end='')
print(' and ' + spam[-1])
