# 8 character long
# upper and lowercase
# 1 digit

import re
lowercase = re.compile(r'[a-z]+')
uppercase = re.compile(r'[A-Z]+')
one_digit = re.compile(r'\d+')
lenght = re.compile(r'.{8,}')
strong_password = [lowercase, uppercase, one_digit, lenght]

password = "YuuKii56855_"
solidity = 0
for checks in strong_password:
    if checks.search(password):
        solidity += 1
if solidity > 3:
    print('Your password is valid')
else: 
    print('Please choose an other password. It has to contains at least a number, an uppercase and a lowercase and be 8 characters long.')
