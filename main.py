# DAY 70 2025-04-23 (Wednesday)

# import flask to use it
from flask import Flask, render_template # render_template() has to be imported from Flask

# instantiate your application - initialization of Flask
# flask instance
app = Flask(__name__)

#__name__ - special built-in variable that represents the name of the current file where the application is built.
#         - tells Flask where the project starts

@app.route('/') # function 1
def home() : # function 2
    # name = "Simmy Shiundu"
    # return render_template("index.html",data = name)

    # user = {"name":"Simmy","location":"Nairobi"}
    # return render_template("index.html",data = user)

    numbers = [1,2,3,4,5]
    return render_template("index.html",data = numbers)

# def print_name() :
#     print("Michael")

# DAY 71 2025-04-24 (Thursday)

# running the application
@app.route('/products') 
def products() : 
    return render_template("products.html")

@app.route('/sales') 
def sales() : 
    return render_template("sales.html")

@app.route('/orders') 
def orders() : 
    return render_template("orders.html")

# run your app
app.run(debug=True) # watchdog - way to track errors

#inheritance => parent class and child class have similar properties
#encapsulation => combining data and functions
