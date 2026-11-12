import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004"
)

# Create cursor
mycursor = mydb.cursor(buffered=True)


# Task 1: Create database
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS store_db")
    print("Database created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()


# Task 2: Create customers table
try:
    mycursor.execute("USE store_db")

    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        email VARCHAR(100)
    )
    """)

    print("Customers table created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()

# Task 3: Create products table
try:
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INT PRIMARY KEY AUTO_INCREMENT,
        product_name VARCHAR(100),
        price DECIMAL(10,2),
        stock INT
    )
    """)

    print("Products table created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()

# Task 4: Create customer_products table
try:
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customer_products (
        customer_id INT,
        product_id INT,
        quantity INT,
        PRIMARY KEY (customer_id, product_id),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    print("Customer_Products table created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()

# # Task 5: Insert customers data
try:
    query = """
    INSERT INTO customers (name, email)
    VALUES (%s, %s)
    """

    values = [
        ("Ahmed", "ahmed@gmail.com"),
        ("Mohammed", "mohammed@gmail.com"),
        ("Ali", "ali@gmail.com"),
        ("Khalid", "khalid@gmail.com"),
        ("Omar", "omar@gmail.com")
    ]

    mycursor.executemany(query, values)
    mydb.commit()

    print("Customers inserted successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()


# # Task 6: Insert products data
try:
    query = """
    INSERT INTO products (product_name, price, stock)
    VALUES (%s, %s, %s)
    """

    values = [
        ("Laptop", 3500.00, 10),
        ("Mouse", 100.00, 50),
        ("Keyboard", 200.00, 30),
        ("Monitor", 800.00, 15),
        ("Headphones", 250.00, 25)
    ]

    mycursor.executemany(query, values)
    mydb.commit()

    print("Products inserted successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()

# # Task 7: Insert purchase records
try:
    query = """
    INSERT INTO customer_products (customer_id, product_id, quantity)
    VALUES (%s, %s, %s)
    """

    values = [
        (1, 1, 2),
        (1, 2, 1),
        (2, 2, 3),
        (2, 3, 1),
        (3, 3, 2),
        (3, 4, 1),
        (4, 4, 2),
        (4, 5, 1),
        (5, 5, 3),
        (5, 1, 1)
    ]

    mycursor.executemany(query, values)
    mydb.commit()

    print("Purchase records inserted successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()

# Task 8: Retrieve customers and their purchased products
try:
    mycursor.execute("""
    SELECT customers.name, products.product_name, customer_products.quantity
    FROM customers
    INNER JOIN customer_products
    ON customers.customer_id = customer_products.customer_id
    INNER JOIN products
    ON customer_products.product_id = products.product_id
    """)

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print()

# Task 9: Retrieve products purchased by a specific customer
try:
    query = """
    SELECT products.product_name, customer_products.quantity
    FROM customer_products
    INNER JOIN products
    ON customer_products.product_id = products.product_id
    WHERE customer_products.customer_id = %s
    """

    mycursor.execute(query, (1,))

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print()

#Task 10: Update purchase quantity
try:
    query = """
    UPDATE customer_products
    SET quantity = %s
    WHERE customer_id = %s AND product_id = %s
    """

    mycursor.execute(query, (5, 1, 1))
    mydb.commit()

    print("Purchase quantity updated successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()

# Task 11: Delete purchase record
try:
    query = """
    DELETE FROM customer_products
    WHERE customer_id = %s AND product_id = %s
    """

    mycursor.execute(query, (1, 2))
    mydb.commit()

    print("Purchase record deleted successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()



#Task 12: Create UNIQUE index on email
try:
    mycursor.execute("""
    CREATE UNIQUE INDEX idx_email
    ON customers(email)
    """)

    print("Unique index created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()


#  Task 12.1: Handle duplicate email
try:
    query = """
    INSERT INTO customers (name, email)
    VALUES (%s, %s)
    """

    mycursor.execute(query, ("Fahad", "ahmed@gmail.com"))
    mydb.commit()

    print("Customer inserted successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print()

# Task 13: Create normal index on product_name
try:
    mycursor.execute("""
    CREATE INDEX idx_product_name
    ON products(product_name)
    """)

    print("Product name index created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()


# Task 14: Create stored procedure
try:
    mycursor.execute("""
    CREATE PROCEDURE GetProductsByPrice(IN min_price DECIMAL(10,2))
    BEGIN
        SELECT *
        FROM products
        WHERE price >= min_price;
    END
    """)

    print("Stored procedure created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

print()

# Task 15: Execute stored procedure
try:
    mycursor.callproc("GetProductsByPrice", (500,))

    for result in mycursor.stored_results():
        print(result.fetchall())

except mysql.connector.Error as err:
    print("Error:", err)

print()


# Close cursor and connection
try:
    mycursor.close()
    mydb.close()

    print("Connection closed successfully!")

except mysql.connector.Error as err:
    print("Error:", err)
