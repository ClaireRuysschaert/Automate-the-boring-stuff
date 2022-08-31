#Saves and loads pieces of text to the clipboard
# Usage: py.exe emcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe emcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe emcb.pyw list - Loads all keywords to clipboard.

#Extending the multi clipboard
## py.exe emcb.pyw del <keyword> - Delete keyword to clipboard
## py.exe emcb.pyw del all - Delete all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('emcb')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# Delete a keyword content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    else:
        pass

# Detete all keyword contents
if len(sys.argv) == 3 and sys.argv[2].lower() == 'all':
    mcbShelf.clear()

mcbShelf.close()
