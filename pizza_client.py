# import the required modules
from flask import Flask, redirect, url_for, render_template, request
import socket
import pickle
from datetime import datetime

from connection import connection_manager

# import the socket client classes
from UDPSocketClient import UDPSocketClient
from TCPSocketClient import TCPSocketClient

if connection_manager.default.get_protocol() == "UDP":
    # create an instance of the UDP socket client class and bind it to an ip and port
    udp_socket_client = UDPSocketClient('127.0.0.1', 5001)

# create an instance of Flask
app = Flask(__name__)

# create a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# create a route for the success page
@app.route('/success')
def success():
    return render_template('success.html', order)

# create a route for the order page using a POST method
@app.route('/order', methods=['POST'])
def order():
    # define the date and time
    current_date_time = datetime.now()
    date_time_for_order = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    
    # get the data from the form
    if request.method == 'POST':

        # sest the toppings to an empty list
        toppings = ""
        
        # go through each topping and add it to the list
        for topping in request.form.getlist('toppings'):
            toppings += topping + ", "

        # check if there are toppings
        if toppings == "":
            amount_of_toppings = 0
        else:
            # count the amount of toppings
            amount_of_toppings = len(request.form.getlist('toppings'))
            
        # create an order array and fill it with the data
        order = [
            request.form['name'],
            request.form['street'],
            request.form['house_number'],
            request.form['zip_code'],
            request.form['city'],
            request.form['pizza'],
            request.form['amount'],
            amount_of_toppings,
            toppings,
            date_time_for_order

        ]
        
        # encode the order using pickle
        order_to_send = pickle.dumps(order)
        
        
        
        if connection_manager.default.get_protocol() == "UDP":
            # use the udp socket client to send the order
            udp_socket_client.send_order(order_to_send)
        elif connection_manager.default.get_protocol() == "TCP":
            # use the TCP socket client to send the order
            TCPSocketClient('127.0.0.1', 5001, order_to_send)
        
        # return the order to the success page and pass the order as a variable
        return render_template('success.html', order=order)
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
