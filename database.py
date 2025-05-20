# DAY 67 2025-04-16 (Wednesday)

import psycopg2
from datetime import datetime
# from math import squareroot

# create connection to the database
conn = psycopg2.connect(user='postgres', password='3Scubed3',
                        host='localhost', port='5432', database='myduka')

# execute database operations
cur = conn.cursor()  # cur -> GLOBAL VARIABLE which can be used outside a function can be accessed everywhere around the global environment

# query for displaying data in products table
# cur.execute('select * from products;')

# print('list of tuples in products table')

# products = cur.fetchall()
# for p in products:
#     print(p)

# query for displaying data in sales table
# cur.execute('select * from sales;')

# print('')
# print('list of tuples in sales table')

# sales = cur.fetchall()
# for s in sales:
#     print(s)

# FETCH ALL PRODUCTS TABLE FUNCTION
def fetchProducts() :
    cur.execute('select * from products;')
    products = cur.fetchall()
    return products
    # for p in products:
        # return p -> NOT APPLICABLE
        # print(p)
    
# FETCH ALL SALES TABLE FUNCTION
def fetchSales() :
    # cur -> LOCAL VARIABLE which is used inside a function, hence 'cur' VARIABLE that exists outside a function can be used by a function, it doesn't have to exist inside a function.
    cur.execute('select * from sales;')
    sales = cur.fetchall()
    return sales
    # for s in sales:
        # return s -> NOT APPLICABLE
        # print(s)
    
# print('')
# print('list of tuples in products table using fetchProducts() function')
# fetchProducts()

# print('')
# print('list of tuples in sales table using fetchSales() function')
# fetchSales()


# DAY 68 2025-04-17 (Thursday)

# cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('juice',100.99,150.59,70)")

# from datetime import datetime
now = datetime.now()
# cur.execute(f"insert into sales(pid,quantity,created_at)values(2,55.00,'{now}')")
# conn.commit()

# INSERT TO PRODUCTS TABLE FUNCTION
# def insert_products() :
#     cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('juice',100.99,150.59,70)")
#     conn.commit()

# INSERT TO SALES TABLE FUNCTION
# def insert_sales() :
#     cur.execute(f"insert into sales(pid,quantity,created_at)values(2,55.00,'{now}')")
#     conn.commit()

# insert sales - method 1 - takes values as parameters
def insert_sales2(values) :
    insert = "insert into sales(pid,quantity,created_at)values(%s,%s,'now()');"
    cur.execute(insert,values)
    conn.commit()

# insert sales - method 2 - still takes values as parameters but doesn't use placeholders.
# instead we replace placeholders with {values} parameters in a formatted string.
def insert_sales3(values) :
    insert = f"insert into sales(pid,quantity,created_at)values({values});"
    cur.execute(insert)
    conn.commit()

# DAY 69 2025-04-22 (Tuesday)

# functions assists in reusability/modularity/easier debugging/dynamic
# databases have to have atomicity/integrity

# TASK: Modify your select and insert functions to be able to select and insert data from any table.
# HINT: Let your function take parameters (table). 

def fetch_data(table) :
    cur.execute(f"select * from {table} ;")
    data = cur.fetchall()
    return data

# products = fetch_data('products')
# sales = fetch_data('sales')

# print("")
# print("Products from fetch data function:\n",products)
# print("")
# print("Sales from fetch data function:\n",sales)


# insert products - method 1 - takes values as parameters
def insert_products2(values) :
    # use placeholders
    insert = "insert into products(name,buying_price,selling_price)values(%s,%s,%s);"
    cur.execute(insert,values)
    conn.commit() #saving operations

# product_values = ("Apple",120,150,200)
# product_values1 = ("Banana",130,160,240)
# insert_products2(product_values)
# insert_products2(product_values1)
# products = fetch_data('products')
# print("")
# print("Fetching data after modifying function:\n",products)


# insert products - method 2 - still takes values as parameters but doesn't use placeholders.
# instead we replace placeholders with {values} parameters in a formatted string.
def insert_products3(values) :
    insert = f"insert into products(name,buying_price,selling_price)values{values};"
    cur.execute(insert)
    conn.commit() # save data operations

# product_values2 = ("Mango",40,50,100)
# insert_products3(product_values2)
# products = fetch_data('products')
# print("")
# print("Fetching products - Method 2:\n",products)


# method 3 - insert data into multiple tables with varying number of columns
# insert into <table_name>(columns)values();
def insert_data(table,columns,values) :
    cur.execute(f"insert into {table}({columns})values{values}") # f => formatted string
    conn.commit()

# table = 'products'
# p_columns = "name,buying_price,selling_price,stock_quantity"
# p_values = ("Avocado",30,40,50)

# table_2 = 'sales'
# s_columns = "pid,quantity,created_at"
# s_values = (2,55.00,"now()")

# insert_data(table,p_columns,p_values)
# products = fetch_data('products')
# print("")
# print("Products data from the last method:\n",products)

# insert_data(table_2,s_columns,s_values)
# products = fetch_data('sales')
# print("")
# print("Sales data from the last method:\n",sales)

# DAY 75 2025-04-30 (Wednesday)

# DASHBOARD FUNCTION TO FIND PROFIT PER PRODUCT
def profit_per_product() :
    cur.execute("select products.name, sum((products.selling_price - products.buying_price) * sales.quantity) as profit from products inner join sales on products.id = sales.pid group by products.name;")
    profit_per_product = cur.fetchall()
    return profit_per_product

profit_p_product = profit_per_product()
print("Profit per product: ",profit_p_product)

# DASHBOARD FUNCTION TO FIND PROFIT PER DAY
def profit_per_day() :
    cur.execute("select date(sales.created_at), sum((products.selling_price - products.buying_price) * sales.quantity) as profit from products inner join sales on products.id = sales.pid group by sales.created_at;")
    profit_per_day = cur.fetchall()
    return profit_per_day

profit_p_day = profit_per_day()
print("Profit per day: ",profit_p_day)

# DASHBOARD FUNCTION TO FIND SALES PER PRODUCT
def sales_per_product() :
    cur.execute("select products.name, sum(products.selling_price * sales.quantity) as revenue from products inner join sales on products.id = sales.pid group by products.name;")
    sales_per_product = cur.fetchall()
    return sales_per_product

sales_p_product = sales_per_product()
print("Sales per product: ",sales_p_product)

# DASHBOARD FUNCTION TO FIND SALES PER DAY
def sales_per_day() :
    cur.execute("select date(sales.created_at), sum(products.selling_price * sales.quantity) as revenue from sales inner join products on products.id = sales.pid group by sales.created_at;")
    sales_per_day = cur.fetchall()
    return sales_per_day

sales_p_day = sales_per_day()
print("Sales per day: ",sales_p_day)

# DAY 77 2025-05-05 (Monday)

# Create the users' table on myduka database

# cur.execute("create table users(id serial primary key, full_name varchar(255) not null, phone_number varchar(255) not null, email varchar(255) unique not null, password varchar(255) not null);")


# DAY 78 2025-05-06 (Tuesday)

def check_user(email) :
    query = "select * from users where email = %s;"
    cur.execute(query,(email,)) # comma tells python that data is a tuple.
    user = cur.fetchone() # fetchall() returns a list of tuples, while fetchone() returns one tuple.
    return user

def add_user(user_details) :
    query = "insert into users(full_name,phone_number,email,password)values(%s,%s,%s,%s);"
    cur.execute(query,user_details)
    conn.commit() # commit changes made to the database
    cur.close() # closes database session

# fetch stock
def fetchStock() :
    cur.execute('select * from stock;')
    stock = cur.fetchall()
    return stock

# get stock
def get_stock(pid) :
    query = "select stock_quantity from stock where pid = %s;"
    cur.execute(query,(pid,))
    stock = cur.fetchone()
    return stock
    # conn.commit()

# add stock - method 1 - takes values as parameters
def insert_stock(values) :
    insert = "insert into stock(pid,stock_quantity,created_at)values(%s,%s,'now()');"
    cur.execute(insert,values)
    conn.commit()

# get contacts
# def fetchContacts() :
#     cur.execute('select * from contacts;')
#     contacts = cur.fetchall()
#     return contacts

# add contact - method 1 - takes values as parameters
# def add_contact(values) :
#     insert = "insert into contacts(full_name,email_address,phone_number,message)values(%s,%s,%s,%s);"
#     cur.execute(insert,values)
#     conn.commit()

# coalesce can return zero(0) which is not NULL/empty value 
def available_stock(pid) :
    cur.execute("select coalesce(sum(stock.stock_quantity), 0) from stock where pid = %s;", (pid,))
    total_stock = cur.fetchone()[0]
    cur.execute("select coalesce(sum(sales.quantity), 0) from sales where pid = %s;", (pid,))
    total_sold = cur.fetchone()[0] or 0
    return total_stock - total_sold

def product_name(pid) :
    cur.execute("select name from products where id = %s;", (pid,))
    product = cur.fetchone()[0] or "Unknown Product"
    return product

def edit_product(values) :
    cur.execute("update products set name = %s,buying_price = %s,selling_price = %s where id = %s;", values)
    conn.commit()
    