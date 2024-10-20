
numeri = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
quadrati = [x**2 for x in numeri]
print(quadrati)

# --------------------------------------------- #

numeriPari =[x for x in range(10) if x % 2 == 0]
print(numeriPari)

# --------------------------------------------- #

def cubo(x):
    return x**3

cubi =[cubo(x) for x in range(10)]
print(cubi)

# --------------------------------------------- #

parole = ["ciao","a","python","ape","cigliegina"]
parole_lunghe =[parola for parola in parole if len(parola) > 3]
print(parole_lunghe)

# --------------------------------------------- #

frutti=["mela","pera","banana"]
maiuscole = [frutto.upper() for frutto in frutti]
print(maiuscole)

# --------------------------------------------- #

valori=["a","b","c"]
tuples=[(i, valore) for i, valore in enumerate(valori)]
print(tuples)

# --------------------------------------------- #

matrice = [[i * j for j in range(3)] for i in range(3)]
print(matrice)

# --------------------------------------------- #

numeri = [1,2,3,4,5,6,7,8,9,10]
numeriSommatiDispari = sum([x for x in numeri if x % 2 != 0])
print(numeriSommatiDispari) 