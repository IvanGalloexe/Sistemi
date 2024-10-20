dati = [1,2,'ciao',3.5, [1,2], None, 10, 'mondo', 3.14]

def controllo(lista):

    
    listaString = []
    listaNumeri = []

    for i in range(len(dati)):
        if isinstance(dati[i], int):
            listaNumeri.append(dati[i])
        elif isinstance(dati[i], str):
            listaString.append(dati[i])
        else: "NONE"
        

    somma = 0
    for i in range(len(listaNumeri)):
        somma += listaNumeri[i]

    media = somma / len(listaNumeri)

    return listaNumeri, somma, media


listaFinale, somma, media = controllo(dati)

print(listaFinale)
print(somma)
print(media)

def listaSommaMedia



def sommaeMedia(dati):
    somma = 0
    listaNumeri = controllo(dati)


    for i in range(len(listaNumeri)):
        somma = i

    media = somma/len(listaNumeri)
print(sommaeMedia(dati))

    
