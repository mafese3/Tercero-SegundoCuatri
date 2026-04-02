from apendiceA import *

private_key_alice = cargar_RSAKey_Privada("./Ciberseguridad/Prácticas/practica3/claves/alice_k_priv.pem", "contrasena_Alice")
public_key_bob = cargar_RSAKey_Publica("./Ciberseguridad/Prácticas/practica3/claves/bob_k_pub.pub")

mensaje_cifrado = cifrarRSA_OAEP("Hola amigos de la seguridad", public_key_bob)
firma_cifrada = firmarRSA_PSS("Hola amigos de la seguridad", private_key_alice)

archivo = open("./Ciberseguridad/Prácticas/practica3/mensajeAlice/mensaje.bin", "wb")
archivo.write(mensaje_cifrado)
archivo.close()

archivo = open("./Ciberseguridad/Prácticas/practica3/mensajeAlice/firma.bin", "wb")
archivo.write(firma_cifrada)
archivo.close()