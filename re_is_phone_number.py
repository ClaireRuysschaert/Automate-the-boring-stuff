import re
#1 Creating Regex object :
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}') 
    # variable contains a Regex object
    # \d = digit character
    # \d\d\d = \d{3}

#2 Matching regex object
mo = phone_num_regex.search('My number is 415-555-4242.')
# match objects
print('Phone number found: ' + mo.group())