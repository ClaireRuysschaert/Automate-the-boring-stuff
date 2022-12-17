# Takes 2 integers and a filename string as command line arguments 
    # N = row where the insertion happens
    # M = number of row inserted
    # filename 

import sys
import openpyxl

insertion_row = int(sys.argv[1])
number_of_row_inserted = int(sys.argv[2])
filename_to_open = sys.argv[3]

wb = openpyxl.load_workbook(filename_to_open)
ws = wb.active
ws.insert_rows(insertion_row,number_of_row_inserted)
wb.save('inserted row file.xlsx')

print(insertion_row, number_of_row_inserted, filename_to_open)
