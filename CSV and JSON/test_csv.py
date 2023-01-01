import csv
from pathlib import Path

# reader and writer obj (use lists)
exemple_file = open(Path.cwd() / "example.csv")
example_reader = csv.reader(exemple_file) #file obj
exemple_data = list(example_reader)
print(exemple_data)
# access value with exemple_data[row][column]

#writer object : list argument to CSV file = writerow()
outputFile = open('output.csv', 'w', newline='') #write mode
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

#rows double spaced or separate with a tab character
csvFile = open('example.tsv', 'w', newline='') #tab separated values
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvFile.close()

#if Header = DictReader and DictWriter obj (use dictionaries)
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
