# DAY 70 2025-04-23 (Wednesday)

# import flask to use it
# render_template() has to be imported from Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import fetchProducts, fetchSales, insert_products2, insert_sales2, profit_per_product, profit_per_day, sales_per_product, sales_per_day, check_user, add_user, fetchStock, insert_stock, available_stock, edit_product
from flask_bcrypt import Bcrypt
from functools import wraps # decorator function which starts with '@' & influences the behaviour of another function

# instantiate your application - initialization of Flask
# flask instance
app = Flask(__name__)
app.secret_key = 'myduka1' # secures data

# __name__ - special built-in variable that represents the name of the current file where the application is built.
#         - tells Flask where the project starts

bcrypt = Bcrypt(app)

@app.route('/')  # function 1
def home():  # function 2
    # name = "Simmy Shiundu"
    # return render_template("index.html",data = name)

    # user = {"name":"Simmy","location":"Nairobi"}
    # return render_template("index.html",data_dict = user)

    # numbers = [1,2,3,4,5]
    # return render_template("index.html",numbers = numbers)
    
    return render_template("index.html")

# def print_name() :
#     print("Michael")
#     return "Michael"

# return render_template("file_name.html",variable = value)

# DAY 71 2025-04-24 (Thursday)

# running the application

def login_required(f) : # login_required() implements decorator function with @wraps()
    @wraps(f) # decorator function influences the behaviour of another function
    def protected(*args,**kwargs) : # function to be called everytime a function is executed. kwargs -> key word arguments
        if 'email' not in session :
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route('/products')
@login_required
def products() :
    products = fetchProducts()
    return render_template("products2.html",products = products)

@app.route('/add_products',methods = ['GET', 'POST'])
def add_products() :
    if request.method == 'POST':
        product_name = request.form['p-name']
        buying_price = request.form['b-price']
        selling_price = request.form['s-price']
        new_product = (product_name, buying_price,
                       selling_price)
        insert_products2(new_product)
        return redirect(url_for('products'))
    
@app.route('/update_product',methods = ['GET','POST'])
def update_product() : # same as edit_product() function in database.py
    if request.method == 'POST' :
        product_name = request.form['p-name']
        buying_price = request.form['b-price']
        selling_price = request.form['s-price']
        product_id = request.form['p-id']
        edited_product = (product_name,buying_price,selling_price,product_id)
        edit_product(edited_product)
        flash("Product edited successfully","success")
        return redirect(url_for('products'))

@app.route('/sales')
def sales() :
    products = fetchProducts()
    sales = fetchSales()
    return render_template("sales.html",sales = sales,products = products)

@app.route('/make_sale',methods = ['POST'])
def make_sale() :
    # if request.method == 'POST' :
    product_id = request.form['p-id']
    quantity = request.form['quantity']
    new_sale = (product_id, quantity)
    # created_at = request.form['created-at'] created_at NOT INCLUDED => self-generated because of 'now()' function
    stock_available = available_stock(product_id)

    if stock_available < float(quantity) :
        flash("Insufficient stock","info")

    insert_sales2(new_sale)
    flash("Sale made successfully","success")
    return redirect(url_for('sales'))

@app.route('/dashboard')
@login_required
def dashboard() :
    profit_p_product = profit_per_product()
    sales_p_product = sales_per_product()

    profit_p_day = profit_per_day()
    sales_p_day = sales_per_day()

    # type conversion / type casting - changing data from one datatype to another. NB: data is usually sent in string form.
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

    return render_template("dashboard.html",product_name = product_name,p_profit = p_profit,p_sales = p_sales,date = date,p_day = p_day,s_day = s_day)

@app.route('/orders')
def orders() :
    return render_template("orders.html")

@app.route('/items')
def items() :
    items = ['chair','desk','table']
    return render_template("items.html",items = items)

@app.route('/sample')
def sample() :
    return render_template("sample.html")

@app.route('/contact-us')
def contact_us() :
    # contacts = fetchContacts()
    return render_template("contact_us.html")

@app.route('/add_contact',methods = ['GET','POST'])
def add_contact() :
    if request.method == 'POST' :
        full_name = request.form['full-name']
        email_address = request.form['email-address']
        phone_number = request.form['phone-number']
        message = request.form['message']
        new_contact = (full_name, email_address, phone_number, message)
        add_contact(new_contact)
        flash("Contact added","success")
        return redirect(url_for('contact-us'))

@app.route('/register',methods = ['GET','POST'])
def register() :
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
            flash("User not found, please register","danger")
            return redirect(url_for('register'))
        else :
            if bcrypt.check_password_hash(user[-1],password) :
                flash("Logged in","success")
                session['email'] = email
                return redirect(url_for('dashboard'))
            else :
                flash("Passwords don't match","danger")
                print('Wrong password')
                
    return render_template("login.html")

# DAY 80 2025-05-07 (Thursday)

# login_required() function MUST BE defined ABOVE decorator functions

# def login_required(f) : # login_required() implements decorator function with @wraps()
#     @wraps(f) # decorator function influences the behaviour of another function
#     def protected() : # function to be called everytime a function is executed
#         if 'email' not in session :
#             return redirect(url_for('login'))
#         return protected

# DAY 83 2025-05-13 (Tuesday)

# protecting navbar route
@app.route('/logout') # session.clear => session.pop
@login_required
def logout() :
    session.pop('email',None)
    flash("You have been logged out","info")
    return redirect(url_for('login'))

@app.route('/stock')
def stock() :
    # get products & get stock
    products = fetchProducts()
    stock = fetchStock() # use Jinja to pass values onto HTML page
    return render_template("stock.html",products = products,stock = stock)

@app.route('/add_stock',methods = ['GET','POST'])
def add_stock() :
    if request.method == 'POST' :
        product_id = request.form['p-id']
        stock_quantity = request.form['stock-quantity']
        new_stock = (product_id,stock_quantity)
        insert_stock(new_stock) # use different add_stock() function name
        flash("Stock added","success")
        return redirect(url_for('stock'))
    # pass

# run your app
app.run(debug = True)  # watchdog - way to track errors

# inheritance => parent class and child class have similar properties
# encapsulation => combining data and functions
