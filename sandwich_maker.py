# This program asks users for their sandwich preference

from string import whitespace
import pyinputplus as pyip

dollar_count = 5
bread_choice = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = 'What type of bread would you want ?\n')
protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt = 'What type of protein would you want ?\n')

want_cheese = pyip.inputYesNo(prompt='Do you want some cheese?')
if want_cheese == "yes":
    cheese_choice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt = 'What type of cheese would you want?\n')
    dollar_count += 1
else:
    pass

want_supp = pyip.inputYesNo(prompt='Do you want mayo, mustard, lettuce, or tomato?')
while want_supp == "yes":
    if want_supp == "yes":
        supp_choice = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], prompt = 'Choose a supp so!\n')
        dollar_count +=1
    else:
        pass
    want_supp = pyip.inputYesNo(prompt = 'Would you like an other supp?')

number_of_sandwiches = pyip.inputInt(prompt = "How many sandwiches would you like ?", min=1)

print(f"{number_of_sandwiches*dollar_count}$ please !")
