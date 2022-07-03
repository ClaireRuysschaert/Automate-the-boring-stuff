#function takes a lists of strings and displays it in column
# column have to be right-justified
# 


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


# Find the longest string in the lists : wide of the column
# Store the max width in a list of integers
# 



# For each list into the dict, the function takes the first arg
# The first arg are displays in lign, separated by a space
# the next arg are displays in a lign return


def print_table(table_data, max_lenght):
    max_lenght = 0
    for element in table_data:
        if len(element[0]) > max_lenght:
            max_lenght = len(element[0])
        else:
            continue

    first_column = []
        for element in table_data:
            first_column.append(element[0])
        for word in first_column:
            print(word.rjust(max_lenght))  

max_lenght = print_table(table_data)
print(max_lenght)

