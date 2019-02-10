#! /usr/bin/env python3

# mcb.pyw - This multiclipboard saves and loads pieces of text to the clipboard.

# Usage: ./mcb.pyw save <keyword> - saves to clipboard to keyword.
#       ./mcb.pyw delete <keyword> - deletes keyword from shelf.
#       ./mcb.pyw <keyword> - Loads keyword to clipboard.
#       ./mcb.pyw list - Loads all the keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword from shelf.
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
   
        
elif len(sys.argv) == 2:    
    # List keywords.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Delete all keywords from shelf.
    elif sys.argv[1].lower() == 'deleteall':
        mcbShelf.clear()
    # Load content to clipboard.    
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

    
