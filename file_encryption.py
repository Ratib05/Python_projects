from cryptography import Fernet

file = input("Enter file path: ")
action = input("Encryption or decryption: ").lower()

# Make a key for encyryption and decryption
def generate_key():
    key = Fernet.generate_key()
    
    # Open or make a new file and write the key into it
    with open("encryption_key", "wb") as key_file:
        key_file.write(key)

# Ensure the key inside the file can be used by opening it in read format
def load_key():
    with open("encryption_key", "rb") as key_file:
        return key_file.read()

# This function encrypts the file
def file_encryption(file, key):
    
    # Open the file in read format and save the contents in a variable that the program can work with
    with open(file, "rb") as file_to_encrypt:
        data = file_to_encrypt.read()
    
    # Encrypt the contents of the variable using the key that was made earlier
    encrypted_data = Fernet(key).encrypt(data)
    
    # Open the file again, but in write format. This allows the progam to overwite the plaintext with the ciphertext
    with open(file, "wb") as file_to_encrypt:
        file_to_encrypt.write(encrypted_data)
    print("Encryption successful")

# This function decrypts the file
def file_decryption(file, key):

    # Open the file in read format and save the contents in a variable that the program can work with
    with open(file, "rb") as file_to_decrypt:
        encrypted_data = file_to_decrypt.read()

    # Decrypt the contents of the variable using the key that was made earlier
    data = Fernet(key).decrypt(encrypted_data)

    # Open the file again, but in write format. This allows the progam to overwite the ciphertext with the plaintext
    with open(file, "wb") as file_to_decrypt:
        file_to_decrypt.write(data)
    print("Decryption successful")

if action == "Encryption":
    key = load_key()
    file_encryption(file, key)

elif action == "Decryption":
    key = load_key()
    file_decryption(file, key)

else: 
    print("Invalid action.")