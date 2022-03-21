
from patterns.commands.Command import Command
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

class AddToDatabase(Command):
    def __init__(self, order) -> None:
        self.order = order
        
    def execute(self):
        data = supabase.table("orders").insert({
            "name": self.order.name,
            "street": self.order.street,
            "house_number": self.order.house_number,
            "zip_code": self.order.zip_code,
            "city": self.order.city,
            "pizza": self.order.pizza,
            "amount": self.order.amount,
            "amount_of_toppings": self.order.amount_of_toppings,
            "toppings": self.order.toppings,
            "order_date_time": self.order.date_time
            }).execute()
        # use assert to check if the data was saved
        assert len(data.data) > 0  