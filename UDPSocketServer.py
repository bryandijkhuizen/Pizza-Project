import socket
import pickle

from order import Order


class UDPSocketServer:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        self.bufferSize = 1024
        self.UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDPSocket.bind((IP, PORT))

        # tell the socket to listen
        print("Listening on port: " + str(self.PORT))

    def listen_for_orders(self):
        while (True):
            bytesAddressPair = self.UDPSocket.recvfrom(self.bufferSize)

            datagram = bytesAddressPair[0]
            address = bytesAddressPair[1]

            data = pickle.loads(datagram)

            # create an instance of the order class
            order = Order(data[0], data[1], data[2], data[3],
                          data[4], data[5], data[6], data[7], data[8])

            order.add_to_database()
            order.print_order()
