import socket
import pickle
from order import Order

# create a TCPSocketServer class


class TCPSocketServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)

        while True:
            client, addr = server.accept()
            print("Connected by", addr)

            data_r = client.recv(1024)
            data = pickle.loads(data_r)

            print(data)

            client.close()
