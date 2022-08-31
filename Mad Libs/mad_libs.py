# This program reads in text file et lets the user add their own text

# open the txt file
# stock in a variable
from pathlib import Path
import pprint

raw_file = open(Path.home() / 'Documents' / 'GitHub' / 'Automate the boring stuff' / 'Mad Libs' / 'raw_text_file.txt')
raw_text = raw_file.read()

coma_replace = raw_text.replace(".", "")
split_text = coma_replace.split()

new_text = ''
for word in split_text:
    if word == "ADJECTIVE":
        new_adjective = input('Enter an adjective:')
        new_text = raw_text.replace("ADJECTIVE", new_adjective, 1)
    elif word == 'NOUN':
        new_noun = input('Enter a noun:')
        new_text = new_text.replace("NOUN", new_noun, 1)
    elif word == 'VERB':
        new_verb = input('Enter a verb:')
        new_text = new_text.replace("VERB", new_verb, 1)
    else:
        pass

print(new_text)
new_file = open('new_text.txt', 'w')
new_file.write(pprint.pformat(new_text))
new_file.close()
raw_file.close()