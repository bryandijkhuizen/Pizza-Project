import socket
import pickle

from order import Order

class TCPSocketClient:
    def __init__(self, IP, PORT, order):
        self.IP = IP
        self.PORT = PORT
        self.order = order
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((self.IP, self.PORT))
            self.s.sendall(self.order)
            self.order_confirmation = self.s.recv(1024).decode()
            print(self.order_confirmation)
        

        
        
     