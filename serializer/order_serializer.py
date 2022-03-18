# create an order serializer
# using the Factory Pattern

# import the datatime module
from datetime import datetime

# import the Order class
from models.order import Order

# create a factory pattern Class: OrderSerializer
class OrderSerializer:
    # serialize method that takes an order object and the format
    def serialize(self, order, format):
        # check which format the order is in
        serializer = get_serializer(format)
        # return the serialized order
        return serializer(order)

# create a function that returns the serializer
def get_serializer(format):
        # check which format the order is in
        if format == 'Array':
            return _serialize_to_array
        elif format == 'Order':
            return _serialize_to_order_object
        else:
            raise ValueError(format)
                          
# create a function that returns the serialized order in an array                         
def _serialize_to_array(order):
        # define the date and time
        current_date_time = datetime.now()
        date_time_for_order = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
        
        # sets the toppings to an empty list
        toppings = ""
        
        # go through each topping and add it to the list
        for topping in order.form.getlist('toppings'):
            toppings += topping + ", "

        # check if there are toppings
        if toppings == "":
            amount_of_toppings = 0
        else:
            # count the amount of toppings
            amount_of_toppings = len(order.form.getlist('toppings'))
            
        # create an order array and fill it with the data
        order = [
            order.form['name'],
            order.form['street'],
            order.form['house_number'],
            order.form['zip_code'],
            order.form['city'],
            order.form['pizza'],
            order.form['amount'],
            amount_of_toppings,
            toppings,
            date_time_for_order

        ]
        
        # return the order array
        return order

# create a function that returns pickled order in an object
def _serialize_to_order_object(order):
    # return the order object
    return Order(order[0], order[1], order[2], order[3], order[4], order[5], order[6], order[7], order[8], order[9])
        