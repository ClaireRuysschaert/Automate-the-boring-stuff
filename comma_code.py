list_things = ['apples', 'bananas', 'tofu', 'cats']


# Write a function that "translate" list value to strings
# la valeur retournée sera une string avec un and en avant dernier
# inserer le and en avant dernier et enlever les virgules

def list_translater(list_things):
    if len(list_things) == 1:
        return list_things[0]
    return f'{", ".join(list_things[:-1])}, and {list_things[-1]}'


print(list_translater(list_things))
