# def maFonction(argument1, argument2):
#     print(f"Mon argument 1 vaut : {argument1}")
#     print(f"Mon deuxième argument est {argument2}")

# maFonction("Poulet", "Yuki")

# L'objectif est de créer un programme qui calcule une suite de nombre jusqu'à
# arriver à 1, nommé la séquence de Collatz.
# Le nouvel objectif est de s'assurer que l'utilisateur a bien rentré
# un nombre en gérant les erreurs.

# Définir fonction nommée collatz avec pour argument un nombre appelé number
def collatz(number):
    # Définition de la fonction collatz
    # Si le nombre est pair
    if number % 2 == 0:
        # Retourner le nombre divisé par deux
        return number/2
    # Si le nombre est impair
    elif number % 2 == 1:
        # Retourner le nombre multipli par trois, puis ajouter 1
        return 3*number+1


# Définition du programme
# Demander à l'utilisateur de rentrer un nombre
# Déterminer si la saisie est bonne
# Tant que l'utilisateur n'a pas rentré un nombre, lui demander de
# rentrer un nombre
while True:
    try:
        number = int(input("Enter number: "))
        break
    except ValueError:
        print('Enter a number, please.')

# Tant que le nombre est différent de 1
while number != 1:
    # Appeler la fonction collatz avec pour argument le nombre
    # Stocker le nombre dans une variable
    number = collatz(number)
    # imprimer le nombre calculé
    print(int(number))
