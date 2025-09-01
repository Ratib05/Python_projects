# perform AES encryption and decryption
from Crypto.Cipher import AES

# add and remove padding to ensure data fits into AES block sizes 
from Crypto.Util.Padding import pad, unpad

# generate random key
from Crypto.Random import get_random_bytes

def encrypt(data, key):
    
    # create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)
    
    # pad the plaintext to fit into 16 bytes, then encrypt the plaintext
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    
    # append IV to cipher text then return it
    return cipher.iv +ct_bytes

def decrypt(enc_data, key):
    
    # seperate the IV from the ciphertext
    iv = enc_data[:16]
    ct = enc_data[16:]
    
    # create AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # remove padding and decrypt cipher text
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    
    # convert decrypted bytes to string
    return pt.decode('utf-8')

# generate 16 bit AES key
key = get_random_bytes(16)
data = "Sensitive data that needs encryption"

# encrypt data
encrypted_data = encrypt(data, key)
print("Encrypted Data: ", encrypted_data)

# decrypt data
decrypted_data = decrypt(encrypted_data, key)
print("Decrypted Data: ", decrypted_data)