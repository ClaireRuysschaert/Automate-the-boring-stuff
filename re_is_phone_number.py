import re

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
#\d = any digit number
mo = phone_num_regex.findall("Cell: 415-555-9999 Work: 212-555-0000.")
# mo = match objects
print(mo)

# Review of Regular Expression Matching
# While there are several steps to using regular expressions in Python, each
# step is fairly simple.
# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use
# a raw string.)
# 3. Pass the string you want to search into the Regex object’s search()
# method. This returns a Match object.
# 4. Call the Match object’s group() method to return a string of the actual
# matched text.

#findall():
# ° When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d , the method findall() returns a list of string matches
# ° When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)​-(\d\d\d\d) , the method findall() returns a list of tuples of strings (one string for each group)
