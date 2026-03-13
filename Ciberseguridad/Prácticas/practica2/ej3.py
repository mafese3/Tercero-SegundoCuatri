from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter

class AES_CIPHER_CBC:

    BLOCK_SIZE_AES = 16 # AES: Bloque de 128 bits

    def __init__(self, key):
        self.key = key

    def cifrar(self, cadena, IV):
        """Cifra el parámetro cadena (de tipo String) con una IV específica, y 
           devuelve el texto cifrado binario"""
        data = cadena.encode("utf-8")
        cipher = AES.new(self.key, AES.MODE_CBC, IV)
        ciphertext = cipher.encrypt(pad(data, self.BLOCK_SIZE_AES))
        return ciphertext

    def descifrar(self, cifrado, IV):
        """Descifra el parámetro cifrado (de tipo binario) con una IV específica, y 
           devuelve la cadena en claro de tipo String"""
        decipher = AES.new(self.key, AES.MODE_CBC, IV)
        deciphertext = unpad(decipher.decrypt(cifrado), self.BLOCK_SIZE_AES).decode("utf-8", "ignore")
        return deciphertext

key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16)  # IV aleatorio de 128 bits
datos = "Hola Mundo con AES en modo CBC"
print(datos)
d = AES_CIPHER_CBC(key)
cifrado = d.cifrar(datos, IV)
print(cifrado)
descifrado = d.descifrar(cifrado, IV)
print(descifrado)

