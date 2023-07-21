from datetime import datetime
import email
from .models import products_list
import json
from flask import Blueprint, jsonify, render_template, session, url_for, redirect, request

views = Blueprint('views', __name__)
from .models import empty_cart
from main import mydb
myorders = mydb['myorders']
from .auth import mycarts
@views.route('/', methods=['GET', 'POST'])
def home():
    Logged_in = False
    if 'email' in session:
        Logged_in = True
    return render_template("home.html", plist=products_list, Logged_in=Logged_in)


@views.route('/about')
def about():
    Logged_in = False
    if 'email' in session:
        Logged_in = True
    return render_template('about.html', Logged_in=Logged_in)


@views.route("/myorders")
def get_orders():
    email = session['email']
    order_list = list(myorders.find({'email': email}))
    for order in order_list:
        del order['_id']
        order['orders'] = json.loads(order['orders'])
    return render_template('myorders.html', orders=order_list)


@views.route("/place_order", methods=['GET', 'POST'])
def place_orders():
    if 'email'  in session: 
        orders = request.form['orders']
        new_order = {
            'email': session['email'],
            'orders': orders,
            'date':datetime.now()
        }
        emtpy={
            'email':new_order['email'],
             'orders':json.dumps(empty_cart)
        }
        mycarts.find_one_and_update({'email':new_order['email']},{'$set':emtpy})
        myorders.insert_one(new_order)
    return redirect(url_for('views.get_orders'))
