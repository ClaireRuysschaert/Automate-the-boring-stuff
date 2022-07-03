# Goal : Translate a sentence into pig latin.
# vowel -> yay added to the end of the word
# consonant -> ay added to the end of the word


sentence = 'My name is AL SWEIGART and I am 4,000 years old.'

# Separate each word of the sentence (split) = list
separate_words = sentence.split()

# For ech word, if it is beginning with a vowel, add yay
vowel = ('a', 'e', 'i', 'o', 'u', 'y')
piglatin = []

for word in separate_words:

    # Get rid of the final point and pass the numbers
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        piglatin.append(prefixNonLetters)
        continue
    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()  # Make the word lowercase for translation.

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in vowel:
        prefixConsonants += word[0]
        word = word[1:]

    if word.startswith(vowel) is True:
        word += 'yay'

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word.
    piglatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(piglatin))
