from pathlib import Path
print(Path.home())
p = Path.home() / "hello.txt"
helloFile = open(p)
helloContent = helloFile.read()
print(helloContent)
TDB = Path.home() / "TDB.txt"
tdbfile = open(TDB, "w")
tdbfile.write("TDB est le plus beau de l'univers")
tdbfile = open(TDB, "a")
tdbfile.write("\nExcepté Yuki le magnifique.")