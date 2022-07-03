from unicodedata import name


def ask_name():
    print('What is your name ? ')
    name = input()
    return name

tdb = ask_name()
print('Hello, '+ tdb )
