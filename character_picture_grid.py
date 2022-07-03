# The goal of this code is to print an image of a heart from the grid.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# 0 -- x
# |
# y

# Use a loop in a loop
# Print the first column of the grid [0][0] ... 10 20 30 40 50 60 70 80
# Print the second column of the grid [0][1] .... 11 21 31 41 51 61 71 81
# Print the third column of the grid [0][2]
# Print the fourth fourth of the grid [0][3]
# Print the fifth column of the grid [0][4]
# Print the sixth column of the grid [0][5]

# use end at the end of the print

# Pour chaque ligne de la grille, imprimer le premier élément
for column_position in range(6):
    for lign in grid:
        print(lign[column_position], end='')
    print()
