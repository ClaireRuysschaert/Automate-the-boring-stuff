# Find vowel in a string
import re

vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))

# negative character class = (r'[^]')
consonantRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantRegex.findall("RoboCop eats baby food. BABY FOOD."))

# have to end with = (r'x$'] (dollar sign character)
endsWithNumber = re.compile(r"\d$")
print(endsWithNumber.search("Your number is 42"))

# have to begin with = (r'^x) (caret sign character)
beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello, world!"))

# Carrots cost dollars.

# Wildcard character (. or dot) -> 1 dot = 1 character (exept newline)
atRegex = re.compile(r".at")
print(atRegex.findall("The cat in the hat sat on the flat mat."))

# dot star (match everything exept a newline)
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group())

# dot star + re.DOTALL (match everything)
newlineRegex = re.compile(".*", re.DOTALL)
print(newlineRegex.search("Serve the public trust.\nProtect the innocent.").group())

# case-insensitive matching : re.IGNORECASE or re.I
robocop = re.compile(r"robocop", re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

# substituting strings : sub('str to replace', 'str for the re')
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

