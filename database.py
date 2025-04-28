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
cur.execute('select * from products;')

print('list of tuples in products table')

products = cur.fetchall()
for p in products:
    print(p)

# query for displaying data in sales table
cur.execute('select * from sales')

print('')
print('list of tuples in sales table')

sales = cur.fetchall()
for s in sales:
    print(s)

# FETCH ALL PRODUCTS TABLE FUNCTION
def fetchProducts():

    cur.execute('select * from products;')
    products = cur.fetchall()
    return products
    # for p in products:
        # return p -> NOT APPLICABLE
        # print(p)
    
# FETCH ALL SALES TABLE FUNCTION
def fetchSales():

    # cur -> LOCAL VARIABLE which is used inside a function, hence 'cur' VARIABLE that exists outside a function can be used by a function, it doesn't have to exist inside a function.
    cur.execute('select * from sales')
    sales = cur.fetchall()
    return sales
    # for s in sales:
        # return s -> NOT APPLICABLE
        # print(s)
    
print('')
print('list of tuples in products table using fetchProducts() function')
fetchProducts()

print('')
print('list of tuples in sales table using fetchSales() function')
fetchSales()


# DAY 68 2025-04-17 (Thursday)

cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('juice',100.99,150.59,70)")

# from datetime import datetime
now = datetime.now()

cur.execute(f"insert into sales(pid,quantity,created_at)values(2,55.00,'{now}')")

conn.commit()

# INSERT TO PRODUCTS TABLE FUNCTION
def insert_products() :
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('juice',100.99,150.59,70)")
    conn.commit()

# INSERT TO SALES TABLE FUNCTION
def insert_sales( ) :
    cur.execute(f"insert into sales(pid,quantity,created_at)values(2,55.00,'{now}')")
    conn.commit()

insert_products()
insert_sales()


# DAY 69 2025-04-22 (Tuesday)

# functions assists in reusability/modularity/easier debugging/dynamic
# databases have to have atomicity/integrity


# TASK

# Modify your select and insert functions to be able to select and insert data from any table.
# HINT: Let your function take parameters (table). 

def fetch_data(table) :
    cur.execute(f"select * from {table} ;")
    data = cur.fetchall()
    return data

products = fetch_data('products')
sales = fetch_data('sales')

print("")
print("Products from fetch data function:\n",products)
print("")
print("Sales from fetch data function:\n",sales)


# insert products - method 1 - takes values as parameters
def insert_products2(values) :
    # use placeholders
    insert = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit() #saving operations

product_values = ("Apple",120,150,200)
product_values1 = ("Banana",130,160,240)
insert_products2(product_values)
insert_products2(product_values1)
products = fetch_data('products')
print("")
print("Fetching data after modifying function:\n",products)


# insert products - method 2 - still takes values as parameters but doesn't use placeholders.
# instead we replace placeholders with {values} parameters in a formatted string
def insert_products3(values) :
    insert = f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
    cur.execute(insert)
    conn.commit() # save data operations

product_values = ("Mango",40,50,100)
insert_products3(product_values)
products = fetch_data('products')
print("")
print("Fetching products - Method 2:\n",products)


# method 3 - insert data into multiple tables with varying number of columns
# insert into <table_name>(columns)values();
def insert_data(table,columns,values) :
    cur.execute(f"insert into {table}({columns})values{values}") # f => formatted string
    conn.commit()

table = 'products'
columns = "name,buying_price,selling_price,stock_quantity"
values = ("Avocado",30,40,50)

table_2 = 'sales'
sales_columns = "pid,quantity,created_at"
sales_values = (2,55.00,"now()")

insert_data(table,columns,values)
products = fetch_data('products')
print("")
print("Products data from the last method:\n",products)

insert_data(table_2,sales_columns,sales_values)
products = fetch_data('sales')
print("")
print("Sales data from the last method:\n",sales)
