from hashlib import new
import socket
import pickle

from order import Order


class TCPSocketServer:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
                self.s.bind((self.IP, self.PORT))
                self.s.listen()
                
                print('Waiting for connection...')
                
                self.conn, self.addr = self.s.accept()
                with self.conn:
                    print(f"Connected by {self.addr}")
                    #while True:
                    self.data = pickle.loads(self.conn.recv(1024))
                    if self.data:
                        self.conn.send("Order received".encode())
                        order = Order(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8])                    
                        order.add_to_database()
                        order.print_order() 
                    
            
        
       
       
    
        
            
    