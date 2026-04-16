def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    resultado = ''
    i = 0
    while i < len(cadena):
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + 3) % 26) + 65
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + 3) % 26) + 97
        elif (ordenClaro == 32):
            ordenCifrado = ord(' ')
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    return resultado


def descifradoCesarAlfabetoInglesMAY(cadena):
    resultado = ''
    for letraCif in cadena :
        if(ord(letraCif) >= 65 and ord(letraCif) <= 90):
            letra = ((ord(letraCif) - 65) - 3) % 26 + 65
        elif(ord(letraCif) >= 97 and ord(letraCif) <= 122):
            letra = ((ord(letraCif) - 97) - 3) % 26 + 97
        elif(ord(letraCif) == 32):
            letra = ord(' ')
        resultado = resultado + chr(letra)
    return resultado

print("-------------------- MAYÚSCULAS --------------------")
claroCESARMAY = 'VENI VIDI VINCI AURIA'
print(claroCESARMAY)
cifradoCESARMAY = cifradoCesarAlfabetoInglesMAY(claroCESARMAY) 
print(cifradoCESARMAY)
descifradoCESARMAY = descifradoCesarAlfabetoInglesMAY(cifradoCESARMAY)
print(descifradoCESARMAY)

print("-------------------- minúsculas --------------------")
claroCESARMAY = 'veni vIdI vinCi auRia'
print(claroCESARMAY)
cifradoCESARMAY = cifradoCesarAlfabetoInglesMAY(claroCESARMAY) 
print(cifradoCESARMAY)
descifradoCESARMAY = descifradoCesarAlfabetoInglesMAY(cifradoCESARMAY)
print(descifradoCESARMAY)

"""  """
def cifradoCesarAlfabetoInglesGEN(cadena, key):
    resultado = ''
    i = 0
    while i < len(cadena):
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + key) % 26) + 65
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) + key) % 26) + 97
        elif (ordenClaro == 32):
            ordenCifrado = ord(' ')
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    return resultado


def descifradoCesarAlfabetoInglesGEN(cadena, key):
    resultado = ''
    for letraCif in cadena :
        if(ord(letraCif) >= 65 and ord(letraCif) <= 90):
            letra = ((ord(letraCif) - 65) - key) % 26 + 65
        elif(ord(letraCif) >= 97 and ord(letraCif) <= 122):
            letra = ((ord(letraCif) - 97) - key) % 26 + 97
        elif(ord(letraCif) == 32):
            letra = ord(' ')
        resultado = resultado + chr(letra)
    return resultado

print('--------------------Generalizado--------------------')
key = 5
claroCESARGEN = 'VENI VIDI VINCI AURIA'
print(claroCESARGEN)
cifradoCESARGEN = cifradoCesarAlfabetoInglesGEN(claroCESARGEN, key)
print(cifradoCESARGEN)
descifradoCESARGEN = descifradoCesarAlfabetoInglesGEN(cifradoCESARGEN, key)
print(descifradoCESARGEN)