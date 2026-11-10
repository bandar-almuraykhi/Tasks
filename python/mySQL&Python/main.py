import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004"
)

# Create cursor
mycursor = mydb.cursor()

# Create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
print("Database created successfully!")

# Select database
mycursor.execute("USE school_db")

# Create students table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")
print("Students table created successfully!")

# Create teachers table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50)
)
""")
print("Teachers table created successfully!")

# Create courses table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(50)
)
""")
print("Courses table created successfully!")


# Insert students data
query = "INSERT IGNORE INTO students (id, name, age) VALUES (%s, %s, %s)"

students = [
    (1, "Ahmed", 22),
    (2, "Mohammed", 23),
    (3, "Ali", 21),
    (4, "Khalid", 24),
    (5, "Fahad", 20)
]

mycursor.executemany(query, students)
mydb.commit()

print("Students inserted successfully!")


# Insert teachers data
query = "INSERT IGNORE INTO teachers (id, name, subject) VALUES (%s, %s, %s)"

teachers = [
    (1, "Omar", "Math"),
    (2, "Saad", "English"),
    (3, "Nasser", "Physics"),
    (4, "Abdullah", "Chemistry"),
    (5, "Yousef", "Computer Science")
]

mycursor.executemany(query, teachers)
mydb.commit()

print("Teachers inserted successfully!")


# Insert courses data
query = "INSERT IGNORE INTO courses (id, course_name) VALUES (%s, %s)"

courses = [
    (1, "Python"),
    (2, "Java"),
    (3, "Database"),
    (4, "Web Development"),
    (5, "Cybersecurity")
]

mycursor.executemany(query, courses)
mydb.commit()

print("Courses inserted successfully!")


# Delete courses table
mycursor.execute("DROP TABLE IF EXISTS courses")

print("Courses table deleted successfully!")


# Close connection
mycursor.close()
mydb.close()

print("Connection closed successfully!")
