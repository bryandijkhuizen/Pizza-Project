import socket
import pickle

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    data = ["hello", "from", "client"]
    data_to_send = pickle.dumps(data)

    #string = input("Enter a string: ")
    # send data
    server.send(data_to_send)
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")

    print("server: ", buffer)
