import socket
from supabase import create_client, Client
import pickle

url: str = "https://oyovzzulhjculwgaqbvc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im95b3Z6enVsaGpjdWx3Z2FxYnZjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY0NjY4ODM2MSwiZXhwIjoxOTYyMjY0MzYxfQ.ObnI1PGKqXWdDIKUNvQXnwTaumFl63icbqQdRiS8sAQ"
supabase: Client = create_client(url, key)

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
        print(self.street + " " + self.house_number)
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