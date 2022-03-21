# import the necessary packages
import socket
import pickle
import hashing.hash_order as encrypter
from serializer.order_serializer import OrderSerializer

# import commands
from patterns.commands.AddToDatabase import AddToDatabase
from patterns.commands.PrintOrder import PrintOrder

# create a UDP Socket Server class
# implement the singleton pattern
class UDPSocketServer():
    # set an instance variable to None
    __instance = None
    
     # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not UDPSocketServer.__instance:
            UDPSocketServer.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return UDPSocketServer.__instance
    
    def __init__(self, IP, PORT):
        # set the IP and PORT
        self.IP = IP
        self.PORT = PORT
        self.serializer = OrderSerializer()
        
        # set the buffer size to 1024
        self.bufferSize = 1024
        
        # create a socket using UDP
        self.UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # bind the socket to the IP and PORT
        self.UDPSocket.bind((IP, PORT))

        # tell the socket to listen
        print("Listening on port: " + str(self.PORT))
        
    # create a method to receive data 
    def listen_for_orders(self):
        
        # listen for data
        while (True):
            # receive the data 
            self.addressPair = self.UDPSocket.recvfrom(self.bufferSize)
            
            # get the data from the address pair
            self.datagram = self.addressPair[0]
            
            # get the address from the address pair
            self.address = self.addressPair[1]
            
            # decode the data
            decrypted_order = encrypter.decrypt_message(self.datagram)

            # use pickle to decode the data
            self.data = pickle.loads(decrypted_order)
            
            # create an instance of the order class
            order = self.serializer.serialize(self.data, 'Order')

            # add the order to the database
            AddToDatabase(order).execute()
            
            # print the order
            PrintOrder(order).execute()
