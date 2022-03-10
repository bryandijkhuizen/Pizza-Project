from flask import Flask, redirect, url_for, render_template, request
import socket
import pickle
from datetime import datetime

from UDPSocketClient import UDPSocketClient
from TCPSocketClient import TCPSocketClient

# udp_socket_client = UDPSocketClient('127.0.0.1', 5001)





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html', order)


@app.route('/order', methods=['POST'])
def order():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.method == 'POST':

        toppings = ""
        for topping in request.form.getlist('toppings'):
            toppings += topping + ", "

        # check if there are toppings
        if toppings == "":
            amount_of_toppings = 0
        else:
            amount_of_toppings = len(request.form.getlist('toppings'))
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
            dt_string

        ]
        order_to_send = pickle.dumps(order)
        # udp_socket_client.send_order(order_to_send)
        TCPSocketClient('127.0.0.1', 5001, order_to_send)
        return render_template('success.html', order=order)
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
