

contador = 0

with open("GutenbergBook.txt") as f:
    for line in f:
        contador += line.count("Simpson")

print("La palabra Simpson se hallo {} veces.".format(contador))

