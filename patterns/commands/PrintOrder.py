
from patterns.commands.Command import Command

class PrintOrder(Command):
    def __init__(self, order) -> None:
        self.order = order
        
    def execute(self) -> None:
        print(self.order.name)
        print(self.order.street + " " + self.order.house_number)
        print(self.order.zip_code)
        print(self.order.city)
        print(self.order.pizza)
        print(str(self.order.amount))
        if self.order.amount_of_toppings != 0:
            print(str(self.order.amount_of_toppings))
        split_toppings = self.order.toppings.split(", ")
        for topping in split_toppings:
            print(topping)
        print(self.order.date_time)