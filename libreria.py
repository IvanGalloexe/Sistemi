
library = {"Non disturbarmi":{"Autore": "Denis","voto": 7},"How to build a car":{"Autore":"Mattia","voto":9},
           "How to be successful":{"Autore":"Serd","voto":8}, "Il sottopalla":{"Autore":"Lucio","voto": 0}}


print("Prima print:")
print(library)
print("-------------------------\n")


def addBook(name, title, mark):
        if name not in library:
            library[title] = {"Autore":name,"voto":mark}

addBook("Desy", "Viaggio tra le formiche", 6)
print(" Seconda print")
print(library)
print("-------------------------\n")

def averageMark():
    finalMark = 0
    mark = 0
    numMark = 0
    for i in library:
        mark += library[i]["voto"]
        numMark += 1
    finalMark = mark/numMark
    return finalMark

averageMark()
print("Terza print")
print("media voti: ",averageMark())
print("-------------------------\n")

##def modifyMark(title, num):
##    mark = num
##    for i in library:
##        if library[i] == title:
##            library["voto"] = mark
##modifyMark("Il sottopalla", 10)
##print("Quarta print")
##print(library)
##print("-------------------------\n")



print("Final print")
print(library)
print("media voti:", averageMark())



