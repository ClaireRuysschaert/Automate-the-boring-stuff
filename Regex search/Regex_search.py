# Opens all .txt files in a folder 
# and searches any lines a user_supplied regular expression

from pathlib import Path
import os
import re 

# Opens all txt files in a folder
target_folder = Path.home() / 'Documents' / 'GitHub' / 'Automate the boring stuff' / 'Regex search' / 'Text files'
text_files_list = os.listdir(target_folder)

re_input = input('What are you searching ? Enter a regex:')
for text_file in text_files_list:
    open_file = open(text_file)
    raw_text = open_file.read()
    regex_to_find = re.compile(re_input)
    mo = regex_to_find.findall(raw_text)
    print('Found : ' + str(mo))
    open_file.close()
