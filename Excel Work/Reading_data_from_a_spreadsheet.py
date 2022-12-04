#script that can read from the census spreadsheet file 
#and calculate statistics for each county

import openpyxl, pprint

# 1. Reads the data from the Excel spreadsheet
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# 2. Counts the number of census tracts in each county
# Make sure the key for this state exists.
    countyData.setdefault(state, {})
# Make sure the key for this county in this state exists.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

# 3. Counts the total population of each county
# Each row represents one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
# Increase the county pop by the pop in this census tract.
    countyData[state][county]['pop'] += int(pop)

# 4. Store into a python program
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
