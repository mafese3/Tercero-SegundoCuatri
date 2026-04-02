from apendiceA import *

priv_bob = cargar_RSAKey_Privada("./Ciberseguridad/Prácticas/practica3/claves/bob_k_priv.pem", "contrasena_Bob")
pub_alice = cargar_RSAKey_Publica("./Ciberseguridad/Prácticas/practica3/claves/alice_k_pub.pub")

texto_cifrado = open("./Ciberseguridad/Prácticas/practica3/mensajeAlice/mensaje.bin", "rb").read()
texto = descifrarRSA_OAEP(texto_cifrado, priv_bob)

print("El texto cifrado es: ", texto)

firma_cifrada = open("./Ciberseguridad/Prácticas/practica3/mensajeAlice/firma.bin", "rb").read()

if(comprobarRSA_PSS(texto,firma_cifrada,pub_alice)):
    print("La firma es válida")
else:
    print("La firma no es válida")