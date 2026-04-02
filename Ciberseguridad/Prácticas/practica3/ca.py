from apendiceA import *;

private_key_alice = crear_RSAKey()
guardar_RSAKey_Privada("./Ciberseguridad/Prácticas/practica3/claves/alice_k_priv.pem", private_key_alice, "contrasena_Alice")
guardar_RSAKey_Publica("./Ciberseguridad/Prácticas/practica3/claves/alice_k_pub.pub", private_key_alice)

private_key_bob = crear_RSAKey()
guardar_RSAKey_Privada("./Ciberseguridad/Prácticas/practica3/claves/bob_k_priv.pem", private_key_bob, "contrasena_Bob")
guardar_RSAKey_Publica("./Ciberseguridad/Prácticas/practica3/claves/bob_k_pub.pub", private_key_bob)