# import socket module
import socket
from supabase import create_client, Client
import pickle


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
    
    data = pickle.loads(datagram)
    
    # insert the order into the database
    data = supabase.table("orders").insert({
        "name": data[0], 
        "street": data[1], 
        "house_number": data[2],
        "zip_code": data[3],
        "city": data[4],
        "pizza": data[5],
        "amount": data[6],
        "extra_toppings": data[7],
        "toppings": data[8],
        }).execute()
    assert len(data.data) > 0
    
    # split toppings into a list of strings by comma
    toppings = data.data[0]["toppings"].split(",")
    
    # print the order
    print(
        data.data[0]["name"] + "\n" 
        + data.data[0]["street"] + " "
        + data.data[0]["house_number"] + "\n"
        + data.data[0]["zip_code"] + "\n"
        + data.data[0]["city"] + "\n"
        + data.data[0]["pizza"] + "\n"
        + str(data.data[0]["amount"]) + "\n"
        + str(data.data[0]["extra_toppings"]) 
    )
    
    # print the toppings
    for topping in toppings:
        print(topping.strip())


