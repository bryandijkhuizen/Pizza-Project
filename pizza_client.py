# import the required modules
from flask import Flask, redirect, url_for, render_template, request
import socket
import pickle

from serializer.order_serializer import OrderSerializer


from config.ConnectionManager import connection_manager

# import the socket client classes
from sockets.UDPSocketClient import UDPSocketClient
from sockets.TCPSocketClient import TCPSocketClient

if connection_manager.default.get_protocol() == "UDP":
    # create an instance of the UDP socket client class and bind it to an ip and port
    udp_socket_client = UDPSocketClient('127.0.0.1', 5001)

# create an instance of Flask
app = Flask(__name__)
serializer = OrderSerializer()

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
    
    
    # get the data from the form
    if request.method == 'POST':
        # get the data from the form
        # use the serializer to serialize the data
        order = serializer.serialize(request, 'Array')
        
        # check which protocol the user wants to use
        if connection_manager.default.get_protocol() == "UDP":
            # use the udp socket client to send the order
            udp_socket_client.send_order(order)
        elif connection_manager.default.get_protocol() == "TCP":
            # use the TCP socket client to send the order
            TCPSocketClient('127.0.0.1', 5001, order)
        
        # return the order to the success page and pass the order as a variable
        return render_template('success.html', order=order)
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000, ssl_context=('cert.pem', 'key.pem'))
    
