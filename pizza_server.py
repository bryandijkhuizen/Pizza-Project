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

# create an order class
class Order:
    def __init__(self, name, street, house_number, zip_code, city, pizza, amount, amount_of_toppings, toppings):
        self.name = name
        self.street = street
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city
        self.pizza = pizza
        self.amount = amount
        self.amount_of_toppings = amount_of_toppings
        self.toppings = toppings
        
    def print_order(self):
        print(self.name)
        print(self.street + self.house_number)
        print(self.zip_code)
        print(self.city)
        print(self.pizza)
        print(str(self.amount))
        print(str(self.amount_of_toppings))
        split_toppings = self.toppings.split(", ")
        for topping in split_toppings:
            print(topping)
            
    def add_to_database(self):
        data = supabase.table("orders").insert({
            "name": self.name,
            "street": self.street,
            "house_number": self.house_number,
            "zip_code": self.zip_code,
            "city": self.city,
            "pizza": self.pizza,
            "amount": self.amount,
            "amount_of_toppings": self.amount_of_toppings,
            "toppings": self.toppings
            }).execute()
        assert len(data.data) > 0   
        

# listen for  datagrams
while (True):
    bytesAddressPair = UDPSocket.recvfrom(bufferSize)
    
    datagram = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    data = pickle.loads(datagram)
    
    # create an instance of the order class
    order = Order(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
    
    order.add_to_database()
    order.print_order()

    
