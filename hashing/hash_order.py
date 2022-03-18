# import required modules

import os
import sys

# module that allows the user to encrypt and decrypt orders
from cryptography.fernet import Fernet


# method to generate a hash key
def generate_key():
    # generate a key
    key = Fernet.generate_key()
    
    # write the key to a file
    with open(os.path.join(sys.path[0], "./hashing/hash.key"), "wb") as key_file:
        key_file.write(key)

# method to load the key
def load_key():
     # opens the key file and loads the key from the file
     # returns the key
     return open(os.path.join(sys.path[0], "./hashing/hash.key"), "rb").read()
    
# method to encrypt the message that takes in the order
def encrypt_message(order):
    # load the key
    key = load_key()
    
    # create a fernet object that uses the key
    fernet = Fernet(key)
    
    # encrypt the order
    encrypted_message = fernet.encrypt(order)
    
    # return the encrypted message
    return encrypted_message


# method to decrypt the message that takes in the encrypted order 
def decrypt_message(encrypted_order):
    # load the key
    key = load_key()
    
    # create a fernet object that uses the key
    fernet = Fernet(key)
    
    # decrypt the order
    decrypted_message = fernet.decrypt(encrypted_order)

    # return the decrypted message
    return decrypted_message



