from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter

print("""--------------------MODO ECB--------------------""")
key = get_random_bytes(16)
BLOCK_SIZE = 16

mensaje = "Hola Amigos de Seguridad"
print("Mensaje: ", mensaje)

cipher = AES.new(key, AES.MODE_ECB)

textoCifrado = cipher.encrypt(pad(mensaje.encode("utf-8"), BLOCK_SIZE))
print("Cifrado: ", textoCifrado)

decipher = AES.new(key, AES.MODE_ECB)

textoDescifrado = unpad(decipher.decrypt(textoCifrado), BLOCK_SIZE).decode("utf-8", "ignore")
print("Descifrado: ", textoDescifrado)


print("""--------------------MODO CTR--------------------""")
key = get_random_bytes(16)
BLOCK_SIZE = 16
nonce = get_random_bytes(8)

mensaje = "Hola Amigos de Seguridad"
print("Mensaje: ", mensaje)

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

textoCifrado = cipher.encrypt(mensaje.encode("utf-8"))
print("Cifrado: ", textoCifrado)

decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

textoDescifrado = decipher.decrypt(textoCifrado).decode("utf-8", "ignore")
print("Descifrado: ", textoDescifrado)


print("""--------------------MODO OFB--------------------""")
key = get_random_bytes(16)
IV = get_random_bytes(16)
BLOCK_SIZE = 16


mensaje = "Hola Amigos de Seguridad"
print("Mensaje: ", mensaje)

cipher = AES.new(key, AES.MODE_OFB, IV)

textoCifrado = cipher.encrypt(mensaje.encode("utf-8"))
print("Cifrado: ", textoCifrado)

decipher = AES.new(key, AES.MODE_OFB, IV)

textoDescifrado = decipher.decrypt(textoCifrado).decode("utf-8", "ignore")
print("Descifrado: ", textoDescifrado)

print("""--------------------MODO CFB--------------------""")
key = get_random_bytes(16)
IV = get_random_bytes(16)
BLOCK_SIZE = 16

mensaje = "Hola Amigos de Seguridad"
print("Mensaje: ", mensaje)

cipher = AES.new(key, AES.MODE_CFB, IV)

textoCifrado = cipher.encrypt(mensaje.encode("utf-8"))
print("Cifrado: ", textoCifrado)

decipher = AES.new(key, AES.MODE_CFB, IV)

textoDescifrado = decipher.decrypt(textoCifrado).decode("utf-8", "ignore")
print("Descifrado: ", textoDescifrado)

print("""--------------------MODO GCM--------------------""")
key = get_random_bytes(16)
BLOCK_SIZE = 16
nonce = get_random_bytes(16)
mac_len = 16

mensaje = "Hola Amigos de Seguridad"
print("Mensaje: ", mensaje)

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=mac_len)

textoCifrado = cipher.encrypt(mensaje.encode("utf-8"))
print("Cifrado: ", textoCifrado)

decipher = AES.new(key, AES.MODE_GCM, nonce=nonce, mac_len=mac_len)

textoDescifrado = decipher.decrypt(textoCifrado).decode("utf-8", "ignore")
print("Descifrado: ", textoDescifrado)
