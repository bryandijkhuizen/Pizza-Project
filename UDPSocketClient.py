# import socket
import socket

# create a socket class

class UDPSocketClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(1)
        self.bufferSize = 1024
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
    def send_order(self, order):
        self.UDPClientSocket.sendto(order, (self.ip, self.port))
        

