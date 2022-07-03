# Goal = Déterminer si le plateau est valide ou non, selon la position
#        des pièces, déterminé par le dictionnaire.

from collections import Counter

# Dictionnaire contenant la bonne position du plateau.
valid_chess_board = {'1h': 'bking', '6c': 'wqueen', '5c': 'bpawn',
                     '2g': 'bbishop', '5h': 'bqueen', '7c': 'wking',
                     '3d': 'bking'}

# Foncion qui check si le plateau est valide
    # but de la fonction : prend un argument du dictionnaire et retourne
    # true/false selon si le plateau est valide ou non


def is_valid_chess_board(board):

# Check if there is a king
    pieces_count = Counter(board.values())
    number_of_bking = pieces_count['bking']
    number_of_wking = pieces_count['wking']

    if number_of_bking != 1 or number_of_wking != 1:
        return False

# Check number of pieces (max 16)
    # Aller chercher la première position de la valeur du dictionnaire
    # Checker si c'est b ou w - Compteur b / w
    player_black = 0
    player_white = 0

    for list_element in pieces_count.keys():
        if list_element[0] == 'b':
            player_black += 1
        else:
            player_white += 1

    # return false si plus que 16 pièces
    if player_black > 16 or player_white > 16:
        return False

# Check if there is max 8 paws
    # Récupérer le nombre de pions par couleur avec counter (dict)
    number_of_bpawn = pieces_count['bpawn']
    number_of_wpawn = pieces_count['wpawn']

    # Si supérieur 8 = false
    if number_of_bpawn > 8 or number_of_wpawn > 8:
        return False

# Check if there is a valid space
    # Récupérer les keys du dictionnaire
    positions = board.keys()
    # Check si elles sont valides (Décomposer en position numérique / lettres)
    # Pour chaque élement de "positions", couper en 2
    for elements in positions:
        first_element = elements[0]
        second_element = elements[1]
        if int(first_element) < 1 or int(first_element) > 8:
            return False
        if second_element < 'a' or second_element > 'h':
            return False
    return True


is_valid = is_valid_chess_board(valid_chess_board)

if is_valid is True:
    print('Chess board valid.')
else:
    print('Chess board invalid.')
