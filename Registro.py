registro = {"Mario":45,"Cardillo":19,"Paolo":0,"V":64,"John":15, "Girardi": 0, "Ivan":19}
registro["Valentina"] = 20
registro["Iris"] = 19


def media(registro):
    somma = 0
    length = 0
    for i in registro:
        somma += registro[i]
        length += 1
    
    media = somma / length
    return media


def nuovoRegistro(registro, media):
    
    registroNuovo = {}
    for i in registro:
        if(registro[i] > media):
            registroNuovo[i] = registro[i]
    print(registroNuovo)
        
    



print(registro)
print(registro.get("Valentina"))
media = media(registro)
print(media)
nuovoRegistro(registro, media)


    