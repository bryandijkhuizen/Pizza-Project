
# import the necessary packages
# import the socket module
import socket
import ssl

# import the pickle module
import pickle

# import the encryption module
import hashing.hash_order as encrypter

# import the order class/module
from models.order import Order

class TCPSSLSocketClient(object):
    # set an instance variable to None
    __instance = None
    
    # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not TCPSSLSocketClient.__instance:
            TCPSSLSocketClient.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return TCPSSLSocketClient.__instance
    
    def __init__(self, IP, PORT, order):
         # set the IP and PORT and order
        self.IP = IP
        self.PORT = PORT
        self.order = order
        # open a socket and open stream
        with socket.socket(
            # create a socket
            socket.AF_INET, socket.SOCK_STREAM) as self.socket_client:
            self.socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket_client = ssl.wrap_socket(self.socket_client, keyfile="./key.pem", certfile="./cert.pem")
            
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
        
        
