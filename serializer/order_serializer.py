# create an order serializer
    # using the Factory Pattern

import json
import pickle
from datetime import datetime
from models.order import Order

class OrderSerializer:
    def serialize(self, order, format):
        serializer = get_serializer(format)
        return serializer(order)
    
def get_serializer(format):
        if format == 'Array':
            return _serialize_to_array
        elif format == 'Order':
            return _serialize_to_order_object
        else:
            raise ValueError(format)
                          
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
        
        return order
    
def _serialize_to_order_object(order):
    return Order(order[0], order[1], order[2], order[3], order[4], order[5], order[6], order[7], order[8], order[9])
        