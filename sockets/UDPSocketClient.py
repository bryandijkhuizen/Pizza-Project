# import the necessary packages
# import the socket module
import socket

# import the pickle module
import pickle

# import the encryption module
import hashing.hash_order as encrypter

# create a UDP Socket Client class
# implement the singleton pattern
class UDPSocketClient(object):
    # set an instance variable to None
    __instance = None
    
    # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not UDPSocketClient.__instance:
            UDPSocketClient.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return UDPSocketClient.__instance
    
    def __init__(self, IP, PORT):
        # set the IP and PORT
        self.IP = IP
        self.PORT = PORT
        
        # set the buffer size to 1024
        self.bufferSize = 1024
        
        # create a socket using UDP
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  
        
    def send_order(self, order):
        
        # encrypt the order
        # generate the key
        encrypter.generate_key()
        
        # dump the order using pickle
        order_to_send = pickle.dumps(order)
    
        # encrypt the order
        encrypted_order = encrypter.encrypt_message(order_to_send)
        
        # send the order to the server
        self.UDPClientSocket.sendto(encrypted_order, (self.IP, self.PORT))
        

