from apendiceA import *

clavePrivBob = cargar_RSAKey_Privada("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPrivBob.pem", "bob")
clavePubAlice = cargar_RSAKey_Publica("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPubAlice.pub")

textoCifrado = open("./Ciberseguridad/Prácticas/Examen/pr3/ej1/mensaje.bin", "rb").read()
firmaDigital = open("./Ciberseguridad/Prácticas/Examen/pr3/ej1/firma.bin", "rb").read()

texto = descifrarRSA_OAEP(textoCifrado, clavePrivBob)
print("El mensaje descifrado es: ", texto)

if(comprobarRSA_PSS(texto, firmaDigital, clavePubAlice)):
    print("La firma es válida.")
else: 
    print("La firma no es válida.")

