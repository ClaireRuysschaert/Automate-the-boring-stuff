# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
# sys reads the potential command line arguments 


if len(sys.argv) > 1:
# Get address from command line.
    # sys.argv is a list of strings : pass to join() which return a single string
    # sys.argv[0] = program name (chop off)
    address = ' '.join(sys.argv[1:])
    print('hello')
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)