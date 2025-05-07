# DAY 70 2025-04-23 (Wednesday)

# import flask to use it
# render_template() has to be imported from Flask
from flask import Flask, render_template, request, redirect, url_for
from database import fetchProducts, fetchSales, insert_products2, insert_sales2, profit_per_product, profit_per_day, sales_per_product, sales_per_day, check_user, add_user
from flask_bcrypt import Bcrypt

# instantiate your application - initialization of Flask
# flask instance
app = Flask(__name__)

# __name__ - special built-in variable that represents the name of the current file where the application is built.
#         - tells Flask where the project starts

bcrypt = Bcrypt(app)


@app.route('/')  # function 1
def home():  # function 2
    # name = "Simmy Shiundu"
    # return render_template("index.html",data = name)

    # user = {"name":"Simmy","location":"Nairobi"}
    # return render_template("index.html",data_dict = user)

    numbers = [1, 2, 3, 4, 5]
    return render_template("index.html",numbers = numbers)

# def print_name() :
#     print("Michael")
#     return "Michael"

# return render_template("file_name.html",variable = value)

# DAY 71 2025-04-24 (Thursday)

# running the application


@app.route('/products')
def products():
    products = fetchProducts()
    return render_template("products.html",products = products)


@app.route('/add_products',methods = ['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p-name']
        buying_price = request.form['b-price']
        selling_price = request.form['s-price']
        stock_quantity = request.form['quantity']
        new_product = (product_name, buying_price,
                       selling_price, stock_quantity)
        insert_products2(new_product)
        return redirect(url_for('products'))


@app.route('/sales')
def sales():
    products = fetchProducts()
    sales = fetchSales()
    return render_template("sales.html", sales=sales, products=products)


@app.route('/make_sale',methods = ['POST'])
def make_sale():
    # if request.method == 'POST' :
    product_id = request.form['p-id']
    quantity = request.form['quantity']
    new_sale = (product_id, quantity)
    insert_sales2(new_sale)
    return redirect(url_for('sales'))

# @app.route('/make_sales',methods = ['GET','POST'])
# def make_sales() :
#     if request.method == 'POST' :
#         product_id = request.form['p-id']
#         quantity = request.form['quantity']
#         created_at = request.form['created-at'] # created_at NOT INCLUDED => self-generated because of 'now()' function
#         new_sales = (product_id,quantity,created_at)
#         insert_sales2(new_sales)
#         return redirect(url_for('sales'))


@app.route('/dashboard')
def dashboard():
    profit_p_product = profit_per_product()
    sales_p_product = sales_per_product()

    profit_p_day = profit_per_day()
    sales_p_day = sales_per_day()

    # type conversion / type casting
    # list comprehension => RESEARCH:
    product_name = [i[0] for i in profit_p_product]
    p_profit = [float(i[1]) for i in profit_p_product]
    p_sales = [float(i[1]) for i in sales_p_product]

    # day metrics - data
    date = [str(i[0]) for i in profit_p_day]
    # date = [i[0] for i in sales_p_day]
    p_day = [float(i[1]) for i in profit_p_day]
    s_day = [float(i[1]) for i in sales_p_day]

    # return render_template("dashboard.html",profit_p_product = profit_p_product,profit_p_day = profit_p_day,sales_p_product = sales_p_product,sales_p_day = sales_p_day)

    return render_template("dashboard.html", product_name=product_name, p_profit=p_profit, p_sales=p_sales, date=date, p_day=p_day, s_day=s_day)


@app.route('/orders')
def orders():
    return render_template("orders.html",)


@app.route('/items')
def items():
    items = ['chair', 'desk', 'table']
    return render_template("items.html", items=items)


@app.route('/sample')
def sample():
    return render_template("sample.html")


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST' :
        name = request.form['full-name']
        phone_number = request.form['phone-number']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = check_user(email)
        if not user:  # NOT if user == None :
            new_user = (name, phone_number, email, hashed_password)
            add_user(new_user)
            return redirect(url_for('login'))
        else:
            print("Already registered")

    return render_template("register.html")


@app.route('/login',methods = ['GET','POST'])
def login() :
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['password']

        user = check_user(email)
        if not user :
            return redirect(url_for('register'))
        else :
            if bcrypt.check_password_hash(user[-1],password) :
                return redirect(url_for('dashboard'))
            else :
                print('Wrong password')
                
    return render_template("login.html")


# run your app
app.run(debug=True)  # watchdog - way to track errors

# inheritance => parent class and child class have similar properties
# encapsulation => combining data and functions
