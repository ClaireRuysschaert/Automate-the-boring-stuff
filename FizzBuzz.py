"""
Exercice Bonus : FizzBuzz

L'objectif est de créer une fonction nommée Fizzbuzz qui accepte un nombre comme
argument et qui va imprimer des nombres de 1 à "nombre" en remplaçant les
multiples de 3 par "Fizz" et les multiples de 5 par "Buzz".

Par exemple Fizzbuzz(15) donnera :
1
2
Fizz -> 3 est un multiple de 3
4
Buzz -> 5 est un multiple de 5
Fizz -> 6 est un multiple de 3 etc ...
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

Si un nombre est à la fois un multiple de 3 et de 5, alors on
imprimera "FizzBuzz" (par exemple 15 est à la fois multiple de 3 et de 5)
"""
# L'objectif est de demander à un utilisateur de rentrer un nombre. La suite des nombres sera affichée en remplaçant les multibles de 3 par l 'Fizz' et les multiples de 5 par 'Buzz'.
# Si le nombre est un multiple de 3 et de 5, on imprimera "FIzzBuzz"


# Définir la fonction Fizzbuzz qui a pour argument un nombre. Cette fonction va traduire les fizz, buzz et les fizz buzz.
def Fizzbuzz(number):
    # Si le nombre est un multiple de 3 et si le nombre est un multiple de 5, retourner Fizzbuzz
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizzbuzz'
    # Si le nombre est un multiple de 3, retourner le nom Fizz
    elif number % 3 == 0:
        return 'Fizz'
    # Si le nombre est un multiple de 5, retourner le nom Buzz
    elif number % 5 == 0:
        return 'Buzz'
    # Sinon retourner la valeur
    else:
        return number


# Tant que l'utilisateur n'a pas rentré le nombre souhaiter, Vérifier si le nombre est bien un nombre en ajoutant l'exception de l'erreur ValueError
while True:
    try:
        number_max = int(input('Enter a number, please.'))
        break
    except ValueError:
        print('Enter a number, please')

# Imprimer la suite de 1 au nombre (for)
# Stocker le nombre et imprimer
for number in range(1, number_max+1):
    result_of_fizzbuzz = Fizzbuzz(number)
    print(result_of_fizzbuzz)
