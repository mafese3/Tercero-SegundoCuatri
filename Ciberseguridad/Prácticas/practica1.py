print("----------------------------APARTADO A---------------------------------")
def cifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) + 3) % 26) + 65
        elif (ordenClaro == 32):
            ordenCifrado = ordenClaro
        # Añade el caracter cifrado al resultado
        
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

def descifradoCesarAlfabetoInglesMAY(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) - 3) % 26) + 65
        elif (ordenClaro == 32):
            ordenCifrado = ordenClaro
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado


claroCESARMAY = 'VENI VIDI VINCI AURIA'
print(claroCESARMAY)
cifradoCESARMAY = cifradoCesarAlfabetoInglesMAY(claroCESARMAY) 
print(cifradoCESARMAY)
descifradoCESARMAY = descifradoCesarAlfabetoInglesMAY(cifradoCESARMAY)
print(descifradoCESARMAY)


print("----------------------------APARTADO B---------------------------------")
def cifradoCesarAlfabetoIngles(cadena):
    resultado = ''
    i = 0
    while(i<len(cadena)):
        letraM = ord(cadena[i])
        letraC = 0
        if(letraM >= 65 and letraM <= 90):
            letraC = (((letraM - 65) + 3) % 26) + 65
        elif (letraM >= 97 and letraM <= 122):
            letraC = (((letraM - 97) + 3) % 26) + 97
        elif (letraM == 32): 
            letraC = letraM
        resultado += chr(letraC)
        i += 1
    
    return resultado

def descifradoCesarAlfabetoIngles(cadena):
    resultado = ''
    i = 0
    while(i<len(cadena)):
        letraC = ord(cadena[i])
        letraD = 0
        if(letraC >= 65 and letraC <= 90):
            letraD = (((letraC - 65) - 3) % 26) + 65
        elif (letraC >= 97 and letraC <= 122):
            letraD = (((letraC - 97) - 3) % 26) + 97
        elif (letraC == 32): 
            letraD = letraC
        resultado += chr(letraD)
        i += 1
    
    return resultado

mensaje = "El perro de San Roque NO tiene RABO"
print(mensaje)
mensajeCifrado = cifradoCesarAlfabetoIngles(mensaje)
print(mensajeCifrado)
mensajeDescifrado = descifradoCesarAlfabetoIngles(mensajeCifrado)
print(mensajeDescifrado)

print("----------------------------APARTADO C---------------------------------")
def cifradoCesarAlfabetoInglesGeneral(cadena, m):
    resultado = ''
    i = 0
    while(i<len(cadena)):
        letraM = ord(cadena[i])
        letraC = 0
        if(letraM >= 65 and letraM <= 90):
            letraC = (((letraM - 65) + m) % 26) + 65
        elif (letraM >= 97 and letraM <= 122):
            letraC = (((letraM - 97) + m) % 26) + 97
        elif (letraM == 32): 
            letraC = letraM + m
        elif (letraM == 44):
            letraC = letraM + m
        resultado += chr(letraC)
        i += 1
    
    return resultado

def descifradoCesarAlfabetoInglesGeneral(cadena, m):
    resultado = ''
    i = 0
    while(i<len(cadena)):
        letraC = ord(cadena[i])
        letraD = 0
        if(letraC >= 65 and letraC <= 90):
            letraD = (((letraC - 65) - m) % 26) + 65
        elif (letraC >= 97 and letraC <= 122):
            letraD = (((letraC - 97) - m) % 26) + 97
        elif (letraC == 32 + m): 
            letraD = letraC - m
        elif (letraC == 44 + m):
            letraD = letraC - m
        resultado += chr(letraD)
        i += 1
    
    return resultado

mensajeG = "Tengo hambre, me comería una TORTILLA"
print(mensajeG)
mensajeCifradoG = cifradoCesarAlfabetoInglesGeneral(mensajeG, 4)
print(mensajeCifradoG)
mensajeDescifradoG = descifradoCesarAlfabetoInglesGeneral(mensajeCifradoG, 4)
print(mensajeDescifradoG)

