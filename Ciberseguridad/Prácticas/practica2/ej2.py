from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter


#----------------------------- CONSTANTES -----------------------------
key = get_random_bytes(16)
IV = get_random_bytes(16)
BLOCK_SIZE_AES = 8

#----------------------------- MENSAJE -----------------------------
data = "Hola Amigas de Seguridad".encode("utf-8")
print(data)

#[APARTADO A. CIFRADO ECB]
#----------------------------- CIFRADO -----------------------------

""" Usamos el modo ECB tanto para el cifrado como para el descifrado. """
cipherECB = AES.new(key, AES.MODE_ECB) 

ciphertext = cipherECB.encrypt(pad(data,BLOCK_SIZE_AES))
print("Texto cifrado 1 [ECB]: ", ciphertext)

#----------------------------- DESCIFRADO -----------------------------
decipherECB = AES.new(key, AES.MODE_ECB)

new_data = unpad(decipherECB.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
print("Texto descifrado 1 [ECB]: ",new_data)



#[APARTADO B. CIFRADO CTR]
#----------------------------- CIFRADO -----------------------------
NONCE = get_random_bytes(4)
""" Usamos el modo CTR tanto para el cifrado como para el descifrado. """
cipherCTR = AES.new(key, AES.MODE_CTR, nonce=NONCE) 

ciphertext = cipherCTR.encrypt(pad(data,BLOCK_SIZE_AES))
print("Texto cifrado 2 [CTR]: ", ciphertext)

#----------------------------- DESCIFRADO -----------------------------
decipherCTR = AES.new(key, AES.MODE_CTR, nonce=NONCE)

new_data = unpad(decipherCTR.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
print("Texto descifrado 2 [CTR]: ",new_data)



#[APARTADO C. CIFRADO OFB]
#----------------------------- CIFRADO -----------------------------
""" Usamos el modo OFB tanto para el cifrado como para el descifrado. """
cipherOFB = AES.new(key, AES.MODE_OFB, IV) 

ciphertext = cipherOFB.encrypt(pad(data,BLOCK_SIZE_AES))
print("Texto cifrado 3 [OFB]: ", ciphertext)

#----------------------------- DESCIFRADO -----------------------------
decipherOFB = AES.new(key, AES.MODE_OFB, IV)

new_data = unpad(decipherOFB.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
print("Texto descifrado 3 [OFB]: ",new_data)



#[APARTADO D. CIFRADO CFB]
#----------------------------- CIFRADO -----------------------------

""" Usamos el modo CFB tanto para el cifrado como para el descifrado. """
cipherCFB = AES.new(key, AES.MODE_CFB, IV) 

ciphertext = cipherCFB.encrypt(pad(data,BLOCK_SIZE_AES))
print("Texto cifrado 4 [CFB]: ", ciphertext)

#----------------------------- DESCIFRADO -----------------------------
decipherCFB = AES.new(key, AES.MODE_CFB, IV)

new_data = unpad(decipherCFB.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
print("Texto descifrado 4 [CFB]: ",new_data)



#[APARTADO E. CIFRADO GCM]
#----------------------------- CIFRADO -----------------------------
NONCE = get_random_bytes(8)
MAC_LEN = 16
""" Usamos el modo GCM tanto para el cifrado como para el descifrado. """
cipherGCM = AES.new(key, AES.MODE_GCM, nonce=NONCE, mac_len=MAC_LEN) 

ciphertext = cipherGCM.encrypt(pad(data,BLOCK_SIZE_AES))
print("Texto cifrado 5 [GCM]: ", ciphertext)

#----------------------------- DESCIFRADO -----------------------------
decipherGCM = AES.new(key, AES.MODE_GCM, nonce=NONCE, mac_len=MAC_LEN)

new_data = unpad(decipherGCM.decrypt(ciphertext), BLOCK_SIZE_AES).decode("utf-8", "ignore")
print("Texto descifrado 5 [GCM]: ",new_data)