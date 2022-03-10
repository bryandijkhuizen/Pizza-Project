
# import the necessary packages
import socket
import pickle

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
            # send the order to the server
            self.socket_client.sendall(self.order)
            # wait for the data and decode it using pickle
            self.order_confirmation = self.socket_client.recv(1024).decode()
            # if the order was confirmed
            # print the order confirmation
            print(self.order_confirmation)
        

        
        
     