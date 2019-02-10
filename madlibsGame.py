#! /usr/bin/env python3

# Madlibs game replaces placeholder words in text file with user input.

import re

# Create placeholder regex.
placeholder = re.compile(r'NOUN|ADJECTIVE|VERB')

# Open and read the text file with placeholders.
madlib = open('./madlib.txt')
text = madlib.read()
madlib.close()

# Find placeholders one at a time and prompt a replacement.
# Loops until all placeholders found.
while True:
    result = placeholder.search(text)
    if result == None:
        break
    elif result.group() == 'NOUN':
        print('Enter a noun:')
    elif result.group() == 'ADJECTIVE':
        print('Enter an adjective:')
    elif result.group() == 'VERB':
        print('Enter a verb:')
    i = input    
    text = placeholder.sub(i, text, 1)     

# Print text with madlibs and save to new file. 
print(text)
newMadlib = open('./newMadlib.txt', 'w+')
newMadlib.write(text)
newMadlib.close()





