from apendiceA import *;

claveAlice = crear_RSAKey()
guardar_RSAKey_Publica("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPubAlice.pub", claveAlice)
guardar_RSAKey_Privada("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPrivAlice.pem", claveAlice, "alice")

claveBob = crear_RSAKey()
guardar_RSAKey_Publica("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPubBob.pub", claveBob)
guardar_RSAKey_Privada("./Ciberseguridad/Prácticas/Examen/pr3/ej1/kPrivBob.pem", claveBob, "bob")

