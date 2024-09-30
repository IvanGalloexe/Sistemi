lista = [

    [[1,2,3,7],[4,5,6]],
   
    [[7,8,9],[10,11,12,21],[3,4,11]],
   
    [[13,14,15],[16,17,18]]

]

#stampa lista
print(lista)

print(f"lunghezza della lista: {len(lista)}")
print(f"lunghezza della lista [0]: {len(lista[0])}")
print(f"lunghezza della lista [0][0]: {len(lista[0][0])}")
print(f"lunghezza della lista [0][0]: {len(lista[0][1])}")


print(f"range della lista: {range(len(lista))}")
print(f"range della lista [0]: {range(len(lista[0]))}")
print(f"range della lista [0][0]: {range(len(lista[0][0]))}")
print(f"range della lista [0][0]: {range(len(lista[0][1]))}")


for l in range(len(lista)):
    print(l)


for i in range(len(lista)):
    for j in range(len(lista[i])):
        for k in range(len(lista[i][j])):
            lista[i][j][k] += 1
print(lista)


x = 10
print(f"x: vale {x}, tipo: {type(x)}")

x = "ciao"
print(f"x: {x}, tipo: {type(x)}")

x = [1,2,3]
print(f"x: vale {x}, tipo: {type(x)}")


#def si usa per le funzioni
def incrementa(valore):
    #isistance istanza
    if isinstance(valore, int) or isinstance(valore, float):
        return valore + 1 
    elif isinstance(valore, str):
        return valore + "\t aggiunto"
    else:
        return "Tipo non supportato"
    
print(incrementa(5))
print(incrementa(5.5))
print(incrementa("test"))
print(incrementa([1,2,3]))

lista2 = []
lista2.append("ciao")
lista2.append(13)
print(lista2)

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
        
        
    return listaNumeri, listaString
   
#sasso finche non va 

print(controllo(dati))

#prova commit