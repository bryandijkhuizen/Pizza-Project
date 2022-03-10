# import the necessary packages
import socket

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
        
    # create a method to send data
    def send_order(self, order):
        # send the order to the server
        self.UDPClientSocket.sendto(order, (self.IP, self.PORT))
        

