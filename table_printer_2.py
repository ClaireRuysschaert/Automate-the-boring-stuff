# Create a function that organize a dict (list of lists) in r-just
# Verify the lenght of the index in the list 
# Create a list of integers that stores the width of each column
# for each index in the list, print it in a column

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def organizator(table_data):
    lenght_list = []
    for index in table_data[0]:
        lenght_list.append(len(index))
    print(lenght_list)
    lenght_max = max(lenght_list)
    print(lenght_max)
    column_width = []
    column_width.append(lenght_max)
    print(column_width)

organizator(table_data)
# i'm lost in paradise 
# r-just first index and print it and then do it for the rest maybe with an other for loop
# and don't forget enumerate just in case because tdb told us before
# maybe tdb is trying to lost us
# i don't have this information yet