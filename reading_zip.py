import zipfile, os
from pathlib import Path
p = Path.home() / "Documents" / "GitHub" / "Automate the boring stuff"
exampleZip = zipfile.ZipFile(p / 'example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
exampleZip.extractall(str(p))
exampleZip.close()
