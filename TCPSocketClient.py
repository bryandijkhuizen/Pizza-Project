import socket
import pickle

# create TCPSocketClient


class TCPSocketClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.ip, self.port))

        order = ["Dijkhuizen", "Scrhijndijk", "Amsterdam"]
        order_to_send = pickle.dumps(order)
        self.server.send(order_to_send)

    def send_order(self, _order):
        pass
