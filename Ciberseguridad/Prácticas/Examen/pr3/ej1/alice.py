from apendiceA import *;

clavePrivadaAlice = cargar_RSAKey_Privada("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPrivAlice.pem", "alice")
clavePublicaBob = cargar_RSAKey_Publica("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPubBob.pub")

mensaje = "Hola amigos de la seguridad"

mensajeCifrado = cifrarRSA_OAEP(mensaje, clavePublicaBob)
firmaMensaje = firmarRSA_PSS(mensaje, clavePrivadaAlice)

archivo = open("./Ciberseguridad/Prácticas/Examen/pr3/ej1/mensaje.bin", "wb")
archivo.write(mensajeCifrado)
archivo.close()

archivo = open("./Ciberseguridad/Prácticas/Examen/pr3/ej1/firma.bin", "wb")
archivo.write(firmaMensaje)
archivo.close()