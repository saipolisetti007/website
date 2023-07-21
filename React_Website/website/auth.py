from asyncio.windows_events import NULL
from datetime import datetime
import errno
import json
from flask import Blueprint, flash, jsonify,render_template,request, session, url_for,redirect
from werkzeug.security import generate_password_hash,check_password_hash


auth=Blueprint('auth',__name__)
from main import mydb
myusers=mydb["new_users"]
mycarts=mydb["carts"]

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        user=myusers.find_one({'email':email})
        if user:
            if check_password_hash(user['password'],password):
                flash("Login success",category='success')
                session['email']=email
                return redirect(url_for('views.home'))
            else:
                flash("Invalid details",category='error')
        else:
            flash('Invalid Details',category='error')
    return render_template('login.html')

@auth.route("/logout")
def logout():
    try:
        session.pop('email')
    except:
        print("email is not exists")
    flash('logged out succesfully',category='successs')
    return redirect(url_for('views.home'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if 'email' in session:
        flash("You are already logged in.",category='error')
        return redirect(url_for('views.home'))
    if request.method=='POST':
        email=request.form.get('email')
        prev=myusers.find_one({'email':email})
        if prev is None:
            name=request.form.get('name')
            password=request.form.get('password')
            hpass=generate_password_hash(password,method='sha256')
            user={
                'name':name,
                'email':email,
                'date':datetime.now(),
                'password':hpass
            }
            myusers.insert_one(user)
            session['email']=email
            flash("signed up succesfully",category="success")
            return redirect(url_for('views.home'))
        else:
            flash("Email Already Exists!!",category='error')
    return render_template('signup.html')

@auth.route('/employee_login',methods=['GET','POST'])
def employee_login():
    if request.method=='POST':
        return render_template('employee_login.html',level=2)
    return render_template('employee_login.html',level=1)

@auth.route('/employee',methods=['GET','POST'])
def employee_dashboard():
    if request.method=='POST':
        # get the employee id here from details 
        return render_template('employee.html',id="random")

@auth.route('/update_cart',methods=['GET','POST'])
def update_cart():
        if 'email' in session:
            cart={
                'email':session['email'],
                'orders':request.headers.get('Orders')
            }
            print(cart)
            if mycarts.find_one({'email':session['email']}):
                mycarts.find_one_and_update({'email':cart['email']},{'$set':cart})
            else:
                mycarts.insert_one(cart)
            return jsonify({"Logged_in":True})
        else:
            # flash("You are not logged in!!",category='error')
            return jsonify({"Logged_in":False})

@auth.route('/get_cart',methods=['GET','POST'])
def get_cart():
        cart=NULL
        try:
            email=session['email']
            cart=mycarts.find_one({'email':email})
        except:
            pass
        res={}
        if cart is not NULL:
            res={
                'success':True,
                'orders':cart['orders']
            }
        else:
            res={
                'success':False
            }   
        return jsonify(res)
    
