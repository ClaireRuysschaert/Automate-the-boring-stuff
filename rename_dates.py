# Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
# 1. It searches all the filenames in the current working directory for
# American-style dates.
# 2. When one is found, it renames the file with the month and day
# swapped to make it European-style.

# Create a Regex for American-Style Dates
import shutil, os, re
from pathlib import Path

datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)- # one or two digits for the month
((0|1|2|3)?\d)- # one or two digits for the day
((19|20)\d\d) # four digits for the year
(.*?)$ # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory.
p = Path.home() / "Documents" / "GitHub" / "Automate the boring stuff"
p_am = p / "American dates"
p_eu = p / "European dates"

for amerFilename in os.listdir("C:/Users/netcl/Documents/GitHub/Automate the boring stuff/American dates"):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:
        continue
    
# Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# Get the full, absolute file paths.
    print(absWorkingDir = os.path.abspath(p))
    print(amerFilename = os.path.join(p, p_am))
    print(euroFilename = os.path.join(p, p_eu))

    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')

    shutil.move(amerFilename, euroFilename) 
