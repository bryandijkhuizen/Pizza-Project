
# import the necessary packages
# import the socket module
import socket

# import the pickle module
import pickle

# import the encryption module
import hashing.hash_order as encrypter

# import the order class/module
from models.order import Order

# create a TCP Socket class
# implement the singleton pattern
class TCPSocketClient(object):
    # set an instance variable to None
    __instance = None
    
    # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not TCPSocketClient.__instance:
            TCPSocketClient.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return TCPSocketClient.__instance
    
    def __init__(self, IP, PORT, order):
         # set the IP and PORT and order
        self.IP = IP
        self.PORT = PORT
        self.order = order
        
        # open a socket and open stream
        with socket.socket(
            # create a socket
            socket.AF_INET, socket.SOCK_STREAM) as self.socket_client:
            # connect to the server
            self.socket_client.connect((self.IP, self.PORT))
            
            # encrypt the order
            encrypter.generate_key()
            
            # dump the order using pickle
            order_to_send = pickle.dumps(self.order)
            
            # encrypt the order
            encrypted_order = encrypter.encrypt_message(order_to_send)
            
            # send the order to the server
            self.socket_client.sendall(encrypted_order)
            # wait for the data and decode it using pickle
            self.order_confirmation = self.socket_client.recv(1024).decode()
            # if the order was confirmed
            # print the order confirmation
            print(self.order_confirmation)
        

        
        
     