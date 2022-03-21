# import the necessary packages
import socket
import pickle
import hashing.hash_order as encrypter
from serializer.order_serializer import OrderSerializer

# import commands
from patterns.commands.AddToDatabase import AddToDatabase
from patterns.commands.PrintOrder import PrintOrder


from models.order import Order

# create a TCP socket server class
# implement the singleton pattern

class TCPSocketServer():
    # set an instance variable to None
    __instance = None
    
    # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not TCPSocketServer.__instance:
            TCPSocketServer.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return TCPSocketServer.__instance
    
    def __init__(self, IP, PORT):
        # set the IP and PORT
        self.IP = IP
        self.PORT = PORT    
        self.serializer = OrderSerializer()

        
    def listen_for_orders(self):
        # create a socket and open stream
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.socket_server:
                # bind the socket to the IP and PORT
                self.socket_server.bind((self.IP, self.PORT))
                
                # tell the socket to listen for incoming connections
                self.socket_server.listen()
                
                # print a message to the console
                print('Waiting for connection...')
                
                # if there is a connection, accept it
                self.connection, self.address = self.socket_server.accept()
                
                # wait for the connection to be established and open stream for communication
                with self.connection:
                    # if the connection is established, print a message
                    print(f"Connected by {self.address}")
                    
                    # decode the data
                    decrypted_order = encrypter.decrypt_message(self.connection.recv(1024))
                    
                    # wait for the data and decode it using pickle
                    self.data = pickle.loads(decrypted_order)
                    
                    # if there is data
                    if self.data:
                        # send a message to the client that the data has been received
                        self.connection.send("Order received".encode())
                        
                        # create an order instance and fill it with the data
                        order = self.serializer.serialize(self.data, 'Order')
                        
                        # add the order to the database
                        AddToDatabase(order).execute()
                        
                        # print the order
                        PrintOrder(order).execute()
                        
                    # if there is no data
                    else: 
                        # send a message to the client that the data has not been received
                        self.connection.send("Order not received".encode())
                    
            
        
       
       
    
        
            
    