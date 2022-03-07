# import socket module
import socket
from supabase import create_client, Client

# set ip and port
IP = "127.0.0.1"
PORT = 5001

url: str = "https://oyovzzulhjculwgaqbvc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im95b3Z6enVsaGpjdWx3Z2FxYnZjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY0NjY4ODM2MSwiZXhwIjoxOTYyMjY0MzYxfQ.ObnI1PGKqXWdDIKUNvQXnwTaumFl63icbqQdRiS8sAQ"
supabase: Client = create_client(url, key)

# set the buffer size
bufferSize = 1024

# create a socket object
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the IP
UDPSocket.bind((IP, PORT))

# tell the socket to listen
print("Listening on port: " + str(PORT))

# listen for  datagrams
while (True):
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    
    datagram = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    clientMsg = "Message from Client:{}".format(datagram.decode("utf-8"))
    clientIP = "Client IP Address:{}".format(address)
    
    data = supabase.table("orders").insert({"order_name":"Lekkere Pizza"}).execute()
    assert len(data.data) > 0
    
    print(clientMsg)
    print(clientIP)
    


