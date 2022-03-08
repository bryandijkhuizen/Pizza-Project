from cmath import pi
from re import S
import socket
import pickle

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, addr = server.accept()
        print("Connected by", addr)

        data = client.recv(1024)
        printable_data = pickle.loads(data)

        print(printable_data)

        client.close()
