import socket

# create a TCPSocketServer class
class TCPSocketServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        