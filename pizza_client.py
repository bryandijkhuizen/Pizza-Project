from flask import Flask, redirect, url_for, render_template, request
import socket
import pickle
from datetime import date

from UDPSocketClient import UDPSocketClient

udp_socket_client = UDPSocketClient('127.0.0.1', 5001)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/order', methods=['POST'])
def order():
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
            toppings

        ]
        order_to_send = pickle.dumps(order)
        udp_socket_client.send_order(order_to_send)
        return redirect(url_for('success'))
    else:
        return "error"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
