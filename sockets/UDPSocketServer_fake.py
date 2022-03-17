# import the necessary packages
import socket
import pickle


from models.order import Order

# create a UDP Socket Server class
# implement the singleton pattern
class UDPSocketServer_fake():
    # set an instance variable to None
    __instance = None
    
     # create a *magic* method to return the instance
    def __new__(cls, *args, **kwargs):
        # if the instance is None, create a new instance
        if not UDPSocketServer_fake.__instance:
            UDPSocketServer_fake.__instance = object.__new__(cls)
        # otherwise, return the already existing instance
        return UDPSocketServer_fake.__instance
    
    def __init__(self, IP, PORT):
        # set the IP and PORT
        self.IP = IP
        self.PORT = PORT
        
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

            # use pickle to decode the data
            self.data = pickle.loads(self.datagram)
            
            # create an instance of the order class
            order = Order(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8], self.data[9])

            # add the order to the database
            order.add_to_database()
            
            # print the order
            order.print_order()
