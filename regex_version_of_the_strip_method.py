import re
def re_strip(str, strip_character=None):
    strip_beginning = re.compile(r'^\s*')
    strip_end = re.compile(r'\s*$')
    strip_txt = re.compile(f'{strip_character}')
    # string to strip : s have to be removed from the beginning and the end of the str
    
    new_string = ''
    
    if strip_character is None :
        for character in str:
            mo1 = strip_beginning.search(character)
            mo2 = strip_end.search(character)
            if mo1.group() or mo2.group():
                pass
            else:
                new_string += character
    else:
        return strip_txt.sub('', str)
        

    return new_string

print(re_strip('       Hello  ', 'H'))