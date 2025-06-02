DAY 70 2025-04-23 (Wednesday) - Brian

# FLASK

Flask - A microframework used to build applications.

Framework - Software we use to build applications

# Examples of frameworks
- Python frameworks e.g. Flask, Django, FastAPI
- C# frameworks e.g. .NET
- Java frameworks e.g. Spring
- Ruby frameworks e.g. Ruby on Ruby Rails

We use frameworks on top of languages - comes with ready-made libraries for you to build your application.

# Library - Pre-written code that helps you solve specific problems or add certain features.

# Concept of building a house
# Option 1 - Library
Identify land, identify requirements, go to a hardware buy all materials, design the house himself, build the house 
himself.

# Option 2 - Framework
He could go to an architect and engineer and get a pre-designed house (blueprint) with all tools and materials already 
identified and provided. 

A framework is structured hence the programmer has to follow certain conventions and practices 
to achieve the intended goal.

# Examples of libraries

# Framework vs. Library

# concept of house building
# scenario 1 - Awadh's House - library
    He decides to do the entire process himself
    Identify what he needs to build a house e.g land,funds,
    roof,bricks,windows, doors, tools (hammer,nails,saw),wood
    all materials are provided for you and placed in a store
    he starts  building the entire house himself- 
        including design of the house and planning and the actual building


# scenario 2 - Letina's house  - framework
    he decides that scenario 1 is too much work
    he seeks building experts - architect and engineer and the builders
    they give him a design and tools he would need and steps of how the 
    process will take place



# library - will give you tools to use
        - how these tools are to be used is dependent on you
        -flexible to the programmer in usage


# framework - will still give you tools to use but has predefined structure/ rules/conventions
            -usage of these tools is based on these rules
            -rigid /strict in usage
            examples:
            Flask, Django, FastAPI for Python
            .NET for C#
            Spring for Java
            Ruby on Rails for Ruby
            Express for NodeJS


# routing - route
    -mechanism  to map urls to functions - system for resource navigation
    -connects a url to a function in your Flask app
    url - the full address used to access resources on the web
        - e.g www.techcamp.co.ke
            www.microsoft.com
    route - part of the url determines what function to execute when a 
            specific part of the url is accessed
            e.g www.techcamp.co.ke/login
                www.microsoft.com/x-box


# implementation in Python using Flask
@app.route() - decorator function
    -research on what decorator 
    -decorator is function that determines/ allows you to modify the behaviour
    of another function

    -this function can take some parameters:
    1.Rule - the path a user wants to access e.g / , /products, /sales, /about-us
    2.

from flask import Flask

app = Flask(__name__)
#__name__ - special built in variable representing name of the current file
          - helps Flask know where your project is located and where it starts

127.0.0.1:5000- localhost 

#the functions inside created routes have to be unique in naming
#view function is basically the function inside your route

#created a simple flask  app and implemented simple routing
#we've managed to return string data in multiple routes

#can we return something better? - data
return a simple html page - next step

#flask gives you a tool to return html place in place of raw strings
#this tool is a function called render_template()
- a function / tool provided by flask to render/ serve / provide html files
index.html - your page - render_template("index.html")
- this function can take some arguments:
    1.a html page - render_template("index.html")
for this to happen you have t follow some rules / conventions of Flask:
why? - because flask is a framework

flask will require you to have a predefined project structure.

#we were able to return and see our html pages (inside template) in our browser
#next step
-#what more can we return / see using flask? 

render_template() - a function to render html pages
    - can return html pages
    - can also return variables or data inside variable

#return data from flask and send to html
#how do we achieve this? - you have to use tools provided by Flask
                        - you have to follow rules defined by Flask.


# Routing - A mechanism to map URLs to functions - Routing is a system for resource navigation.

# Route - A part of the URL that determines what function to execute when a specific url is accessed or visited.

www.myduka.com/products

www.myduka.com - url
/products - route/rule

# How to implement routing in Flask Framework

@app.route() - decorator function  => # (DEFINTION - WORK TO DO) CHATGPT - decorator function has a prefix - '@'

www.myduka.com/products

@app.route('/products')
def products() :
    products = fetch_data('products')
    return products

@app.route('/login')
def login() :

# What parameters can we pass in a route function?
1. Rule - e.g. /, /products, /sales, /users - defines the path a user accesses in the browser

DAY 71 2025-04-24 (Thursday)

HTTP response status codes
200 - Successful
300/302 - Redirection error
404 - Client error
500 - Server error

We've been returning strings - moving one step forward
# return a simple html page (home page) - serve html pages

            MYDUKA Project Structure
myduka - folder containing entire myduka project
    -main.py
    -database.py
    -templates FOLDER => FIXED name (case-sensitive)
        (all html files MUST be here)
        index.html
        sales.html
        products.html
    -static
        (all static files - files that don't change much)
        -styling => home.css, myduka.css, style.css
        images
        JS files
        favicons - logo icon to identify website
        fonts, pdf files

# Rendering (returning data) - Process of serving html with Flask
Goal: Display a html page/file using Flask

# Implement:
- We render html pages using functions provided by Flask
    render_template() - this function:
        1. has to be imported from Flask in order to be used.
        2. takes some parameters
            i. html pages - (full_name of the html page)
                e.g. render_template("index.html")
            ii. variables holding data

# Create two html files - products.html, sales.html
    - Render them using flask - render_template

# DAY 72 2025-04-25 (Friday)

127.0.0.1 - localhost

# implementing passing data from Flask to html
- to implement this we still have to use tools provided by Flask because Flask is a framework
    # Example of a tool in Flask - Jinja

    # What is Jinja?
        - A templating engine that is integrated with Flask to render (or return) dynamic HTML webpages. {Dynamic - can 
            take some data which changes depending on the user input}
        - Templating engine - A tool in web development used to generate dynamic HTML webpages.

    # What can Jinja do?
        - Helps you pass data or perform Python logic inside HTML templates.

    # How does Jinja work?
        - Pre-defined templates already exist.
        - Passing Jinja syntax inside these templates.
        - Your Flask application provides data to be passed inside Jinja.
        - Data is rendered.

    # What can we pass inside Jinja?
        1. Simple Variables
            - Once you've passed this variable as parameter inside render_template
                i. pass that variable inside Jinja
                    - JINJA SYNTAX {{variable}} NB: Jinja is syntax - programmer writes Jinja.
                    - To pass variable using Jinja, write the correct variable inside two curly braces i.e. {{}}
                        e.g. name = "John Doe"
                             return render_template("index.html",name = name)
                             # inside your HTML (template)
                             <p>Hello {{name}}</p>

        2. Control Structures
            i. Sequence - Executes program sequentially from top to bottom.
            ii. Selection - Executes conditional statememts. e.g. if\else, switch\break
            iii. Iteration - Executes loops i.e. instructions or code until a specified condition is met.
                e.g. for, while, do-while
            
            # Implementing control structures with Jinja
                Jinja syntax when implementing control structures:
                    - {% if %}

                Take Note:
                    - You have to end the program
                    - You have to define a starting point and an ending point

                # Focus on if statememts & loops

                # conditional statements - if
                    x = input()
                    if x < 10 :
                        print("less than 10")
                    else :
                        print("larger than 10")

Task:
    1. Create another list in another route and loop through it using Jinja to pass list values in a html page.

    2. Go and create tables using borrowed css {bootstrap} - use bootstrap to create tables with random data.

# DAY 73 2025-04-28 (Monday)

Display our database data on our browsers

Assumption - You can already view your printed data on your terminal.

1. Get our data to main.py from database.py using import functionality.
    - import functions that fetch data in (products, sales) tables inside main.py.
    - we're going to call these functions inside main.py using variables and then we pass those variables to HTML using 
    Jinja.
    - we want to display our products and sales using tables.
        # GOAL: Make it presentable to a user
    - You want to display each product in their own row, we have to iterate/loop through your data and place each data in 
    a row <tr>.

    - index.html, products.html, sales.html, dashboard.html
    - navbar

# DAY 74 2025-04-29 (Tuesday)

Posting Data

# What is posting?
    - Sending data from a client to a server {Flask} for processing.
    - Client (Web browser, Mobile app) => the entity that sends requests.

# Data flow 
    - User will visit a route
    - User fills out a form and submits it.
    TAKE NOTE: Form action & method {HTTP Method} - Also name attribute
        Action - Route mapping URL to a function e.g. /products, /sales

        Method - HTTP Method: A way of telling Flask/Server what to do with resources.
            e.g. GET, POST, PUT, DELETE
                GET - getting/fetching a resource.
                POST - sending data to a server.
                PUT - update a resource.
                DELETE - delete/erase/get rid of a resource.

- Data is sent to Flask for processing.

- From the action specified Flask will look for a function to execute.
    # In that route, the HTTP method has to be specified as a second parameter in CAPS.
- Flask will extract data from the form using a request object, validates it and saves it.
- User will be redirected back to a page.
    # Redirection - Sends a user to a different route after performing an action like form submission
                  - Used with 'url_for()'
                  SYNTAX: return redirect(url_for(''))

    # request.method
        - An attribute that specifies the HTTP method that the client used when making a request.

    # request.form
        - Allows the user to access/extract data from a form.
        - Mimics a dictionary in the sense that your form data is stored in key-value pairs.
        - The key in this case is the value of the name attribute in the form.

        e.g. "p-name":"eggs"

TASK:
    - Pick a navbar from bootstrap and implement it.
    - Implement the products' form inside a modal from bootstrap.
    - Try posting sales.
    - Start writing queries to fetch sales per day, sales per product, profit per product, profit per day.

# DAY 75 2025-04-30 (Wednesday)

GOAL: Post a sale

Flask implementation is the same with the products implementation.
Table - Sales has a foreign key.
In the sales form:
    - Select dropdown having the products i.e. loop through the products. Pick the pid and name from the iteration.
    - Quantity

Dashboard data:
    - Profit per product.
    - Profit per day.
    - Sales per product.
    - Sales per day.

1. Profit per product
    select products.name, sum((products.selling_price - products.buying_price) * sales.quantity) as profit from products
    inner join sales on products.id = sales.pid group by products.name;

2. Profit per day
    select date(sales.created_at), sum((products.selling_price - products.buying_price) * sales.quantity) as profit from
    products inner join sales on products.id = sales.pid group by sales.created_at;

3. Sales per product
    select products.name, sum(products.selling_price * sales.quantity) as revenue from products inner join sales on
    products.id = sales.pid group by products.name;

4. Sales per day
    select date(sales.created_at), sum(products.selling_price * sales.quantity) as revenue from sales inner join products on
    products.id = sales.pid group by sales.created_at;

TASK: Implement these queries inside functions in database.py and confirm you can see the data in your terminal, pass that
data to dashboard.html using Flask and Jinja.

# DAY 76 2025-05-02 (Friday)

GOAL: Visualize the dashboard data using charts. We'll use charting libraries and implement our charts in a script.
    1. Bar Chart - Helps us represent profit and sales per product.
    2. Line Chart - Visualize any data with a timeframe e.g. date, profit and sales per day.

1. CDN link - content delivery network
2. canvas - where to place your chart in html - element/templating script will know what canvas to place the chart in
    using an id - attribute

    https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/

TAKE NOTE: JavaScript does not recognize Decimal
    - float
    - safe - ignores syntax errors.

TASK:
    - Create a table called 'users' with columns; id, name, email, phone_number.
    - Implement that line chart.

# DAY 77 2025-05-05 (Monday)

Profit per day and Sales per day

Date - Common metric - x-axis
y-axis => profit and sales - how profit compares to sales in relation to dates.

You can fetch date from either profit per day or sales per day
    - both are a list of tuples.
    - each of these tuples has date metric as the first index - date metric is the same in both sales and profit.
    - get that date from sales per day using list comprehension and get that date metric using indices.
        date - index 0 - [0]\

TASK:
- home
- products
- sales
- Dashboard

- have a navbar that can gate to all pages - a footer
styled & descriptive home page giving info about that software/project/POS 
products - modal to add product, products table
sales - modal with form containing a dropdown to select product, table for sale
dashboard - 2 charts along with other relevant information
    - style them completely.
    - datatables.

TASK:
have a register.html webpage inside templates - form
    - name
    - phone_number
    - email
    - password

# Template Inheritance
    - Functionality that allows you create a base template which contains common webpage elements like navbar, headers,
    footers, title e.t.c.

TASK: Create a base.html webpage inside temlates folder
        - have common features in this base.html - footers, navigation, headers
        - have the other templates inherit from the base template.

base.html - base/parent template
    <div class="container">
        Navigation bar
        This is where my header goes
        <div>
            {% block content %}
                // pass whatever is unique to those pages
            {% endblock %}
        </div>
        This is where my footer goes
    </div>

sample.html - other/child template
    {% extends "base.html" %}
    {% block title %} Sample Page {% endblock %}

    {% block content %}
        <p>Welcome to my sample page</p>
    {% endblock %}

# DAY 78 2025-05-06 (Tuesday)

User Registration
- users table

create table users(
    id primary key serial,
    name varchar(100) not null,
    phone_number varchar(255) not null,
    email varchar(255) unique not null,
    password varchar(255) not null
); // NOT case-sensitive

Register route - main.py

    1. Taking user input from a register form.
    2. Check that all inputs are filled correctly.
    3. User posts his/her inforamation.
        - method => POST - defined in the form and route.
        - getting form data => request.form - gets user input posted from a form.
        - request object => request.method - tells server what to do with data.
        - PASSWORD HASHING => converts plain text password into random text i.e. a form that can't be easily understood.
            - encoding.
                - cryptic - for security purposes.
                - bcrypt
                    pip install flask-bcrypt
                    pip show flask-bcrypt

                    from flask_bcrypt import Bcrypt => main.py

                    bcrypt = Bcrypt(app) # initialization

    4. Check if user exists.
        - If user exists : => SELECTS A USER USING THAT EMAIL
            - let the user know they're already registered and tell them to login instead (flash messaging).
        - else :
            - add user => INSERT A USER
            - redirect to login

# have a login form
werkzeug
passlib

# DAY 79 2025-05-07 (Wednesday)

- Getting user info from the user from form.
- Extracting that data using request.
- Check if the user exists:
    - If they don't exist -> redirect to register.
    - If they exist, login -> redirect to dashboard.
        - check user password.
        - bcrypt to compare hashed password and provided password
        - if password is correct,
            - redirect to dashboard.
        - if password is incorrect,
            - flash that password is incorrect.

# DAY 80 2025-05-08 (Thursday)

# FLASH MESSAGING

# FLASHING
    - One time notifications to the user based on user action.
    - Bootstrap colours
        - success (green)
        - error/danger (red)
        - info (blue)
        - warning (yellow)

- import
- replace print() with flash()
- implement flashing in the HTML pages you want it viewed.

NOTE: need secret key to store data in a cookie.

from flask import Flask, flash

Flashing with categories
    https://flask.palletsprojects.com/en/stable/patterns/flashing/

# SESSIONS
    - A way to store user data in between requests.
    - Keeping a user logged in, page protection, storing user preferences.

# DAY 81 2025-05-09 (Friday)

Styling of MYDUKA Project using Bootstrap
    - Cards
    - Carousels
    - Style tables.
    - Get rid of Jinja on Dashboard.
    - Make website look presentable. (RESEARCH)
        - Style 'Home/index.html' webpage/HTML page.
        - Style 'Dashboard'.

# DAY 82 2025-05-12 (Monday) => BIRTHDAY

    WORK ON MYDUKA PROJECT

# DAY 83 2025-05-13 (Tuesday)

delete from sales;
delete from products;

# create a new table called stock
CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    pid INTEGER REFERENCES products(id),
    stock_quantity INTEGER,
    created_at TIMESTAMP
);

# changes to products table
ALTER TABLE products DROP COLUMN stock_quantity;

drop database myduka;
create database myduka;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    buying_price NUMERIC(20, 2),
    selling_price NUMERIC(20, 2)
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    pid INTEGER REFERENCES products(id),
    quantity INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

insert and select for sales/stock.

https://datatables.net/

# DAY 84 2025-05-14 (Wednesday)

1. gotten rid of stock_quantity in products.
2. created a stock table.
3. stock - keeps track of the quantity of products
    - /stock
        - get stock
        - get products

    - /add_stock
        - post stock in this route

making sales
    - check for available stock
        - if insufficient
            - flash relevant info - "Low stock"
        - if sufficient
            - make sale
            - flash "Sale made"

https://datatables.net/examples/styling/bootstrap5.html

pick td with modal
pick the route - update product in main.py
pick update function in database.py

CDN link - Content Delivery Network link

Letting Brian (Contact Info) - Saturday 11.30 a.m.

https://github.con/l-tting

0714056473

# DAY 85 2025-05-17 (Saturday)

Datatables

10
15
20
100
-145 total stock

# making a sale
    - check if you have enough products to sell
        -12
        -20
        -5
        -37 - total sold

availableStock = totalStock - totalSold

null - doesn't exist
0 - actual value

type casting

UPDATE table_name
SET column1 = value1, column = value2, ...
WHERE condition;

