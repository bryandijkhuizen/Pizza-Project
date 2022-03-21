# import the commands module
from patterns.commands.Command import Command

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

        
