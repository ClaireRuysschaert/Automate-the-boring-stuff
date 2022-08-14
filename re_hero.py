import re
heroRegex = re.compile (r'Batman|Tina Fey')
bat_regex = re.compile (r'Bat(man|mobile|copter|bat)')
# | = pipe -> "one of many expressions"
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
mo3 = bat_regex.search('Batmobile lost a wheel')
print(mo1.group(), mo2.group(), mo3.group(), mo3.group(1))

# use findall() il you want all the mo
# without groups : return a list of strings
# with groups : return a list of tuples
