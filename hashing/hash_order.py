import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open(os.path.join(sys.path[0], "./hashing/hash.key"), "wb") as key_file:
        key_file.write(key)

def load_key():
     return open(os.path.join(sys.path[0], "./hashing/hash.key"), "rb").read()
    
def encrypt_message(order):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(order)
    return encrypted_message

def decrypt_message(encrypted_order):
    key = load_key()
    f = Fernet(key)
    
    decrypted_message = f.decrypt(encrypted_order)

    return decrypted_message



