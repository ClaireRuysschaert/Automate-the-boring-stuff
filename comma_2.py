spam = ['apples', 'bananas', 'tofu', 'cats']
# The goal is to create a function that print each element of a list
# and add commas between each and an "and" before last one.
yuki = ['le + beau']
benja = [69, 666]
claire = []


def translator(the_list):
    if the_list is None:
        return

    the_famous_string = str()

    if len(the_list) == 1:
        return the_list[0]

    for element in the_list:
        if element != the_list[-1]:
            the_famous_string = the_famous_string + str(element) + ', '
        else:
            the_famous_string = the_famous_string + 'and ' + str(element)

# Ajouter virgule ou and selon la position dans la liste et l'ajouter
# Dans la variable string

    return the_famous_string


print(translator(spam))
