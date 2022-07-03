# Tring by myself this time, you can do it girl ! 23h20
chess_board = {'1h': 'bking', '6c': 'bqueen', '2g': 'bbishop', '5h': 'bqueen',
               '3e': 'wking', '4d': 'bpawn', '5d': 'bpawn', '6d': 'wpawn'}
# Write a purpose who the goal is to check if the chess board is valid or not.


def is_valid_chess_board(board: dict) -> bool:
    # Check if there is only 1 bking or wking
    # Find the values bking and wking in values in the dict chess_board
    number_of_bking = 0
    number_of_wking = 0
    board_values = board.values()
    # Count the number of bking and wking
    for element in board_values:
        if 'bking' in board_values:
            number_of_bking += 1
        if 'wking' in board_values:
            number_of_wking += 1
    # Check if there is only 1 by color, return False if not
    if number_of_bking != 1 or number_of_wking != 1:
        return False

    # Check if the players have max 16 pieces
    # Use board_values (list of values)
    # Create a variable number_of_pieces
    black_pieces = 0
    white_pieces = 0
    # Count the total number of pieces by color
    for element in board_values:
        # Check if the first letter is b or w and add to the count by color
        if element[0] == 'b':
            black_pieces += 1
        elif element[0] == 'w':
            white_pieces += 1
    # Error if there is more than 16 pieces by players
    if black_pieces > 16 or white_pieces > 16:
        return False

    # Check if there is max 8 pawns
    # Count the number of pawns by color
    number_of_bpawn = 0
    number_of_wpawn = 0
    for element in board_values:
        if element == 'bpawn':
            number_of_bpawn += 1
        if element == 'wpawn':
            number_of_wpawn += 1
    # Error if there is more than 8 pawns by players
    if number_of_bpawn > 8 or number_of_wpawn > 8:
        return False

    # Check if the pieces are in a valid space (1a to 8h)
    # Take the keys of the dictionary =list of keys
    board_keys = board.keys()
    # for each keys element, check the first element and the second if there
    # are in the range
    for element in board_keys:
        if int(element[0]) < 1 or int(element[0]) > 8:
            return False
        if element[1] < 'a' or element[1] > 'h':
            return False
    return True


validity = is_valid_chess_board(chess_board)
print(validity)
