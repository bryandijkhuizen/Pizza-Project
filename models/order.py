# import supabase module
from supabase import create_client, Client

# import os module
import os

# import dotenv module
from dotenv import load_dotenv

# load the .env file
load_dotenv()


# set the key and url for the supabase database
url: str = os.getenv('DB_URL')
key: str = os.getenv('DB_KEY')


# create a supabase client using the url and key
supabase: Client = create_client(url, key)

# create an order class
class Order:
    def __init__(self, name, street, house_number, zip_code, city, pizza, amount, amount_of_toppings, toppings, date_time):
        self.name = name
        self.street = street
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city
        self.pizza = pizza
        self.amount = amount
        self.amount_of_toppings = amount_of_toppings
        self.toppings = toppings
        self.date_time = date_time
        
        
    # create a method to print the order
    def print_order(self):
        print(self.name)
        print(self.street + " " + self.house_number)
        print(self.zip_code)
        print(self.city)
        print(self.pizza)
        print(str(self.amount))
        if self.amount_of_toppings != 0:
            print(str(self.amount_of_toppings))
        split_toppings = self.toppings.split(", ")
        for topping in split_toppings:
            print(topping)
        print(self.date_time)
        
        
    # create a method to save the order to the database        
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
            "toppings": self.toppings,
            "order_date_time": self.date_time
            }).execute()
        # use assert to check if the data was saved
        assert len(data.data) > 0   