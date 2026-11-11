import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="school_db"
)

# Create cursor
mycursor = mydb.cursor(buffered=True)

print("Connected successfully!")
print("\n")


# Task 1.1: Retrieve all students using fetchall()
try:
    mycursor.execute("SELECT * FROM students")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 1.2: Retrieve one student using fetchone()
try:
    mycursor.execute("SELECT * FROM students")

    result = mycursor.fetchone()

    print(result)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 1.3: Retrieve three students using fetchmany()
try:
    mycursor.execute("SELECT * FROM students")

    result = mycursor.fetchmany(3)

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 2: Filter students by age using WHERE
try:
    mycursor.execute("SELECT * FROM students WHERE age > 21")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 3.1: Sort students by age in ascending order
try:
    mycursor.execute("SELECT * FROM students ORDER BY age ASC")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 3.2: Sort students by age in descending order
try:
    mycursor.execute("SELECT * FROM students ORDER BY age DESC")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 4.1: Group students by age
try:
    mycursor.execute("SELECT age FROM students GROUP BY age")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 4.2: Group students by age using COUNT
try:
    mycursor.execute("SELECT age, COUNT(*) FROM students GROUP BY age")

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 5: Update student's age
try:
    mycursor.execute("UPDATE students SET age = 25 WHERE id = 1")

    mydb.commit()

    print("Student updated successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print("\n")


# Task 6: Retrieve students and their courses using INNER JOIN
try:
    mycursor.execute("""
    SELECT students.name, courses.course_name
    FROM students
    INNER JOIN courses
    ON students.id = courses.student_id
    """)

    result = mycursor.fetchall()

    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Task 7: Delete a course using DELETE and WHERE
try:
    mycursor.execute("DELETE FROM courses WHERE id = 5")

    mydb.commit()

    print("Delete executed successfully!")

except mysql.connector.Error as err:
    mydb.rollback()
    print("Error:", err)

print("\n")


# Task 8: Handle database errors using try-except and rollback
try:
    # First update
    mycursor.execute("UPDATE students SET age = 30 WHERE id = 1")

    # Second update (Invalid column)
    mycursor.execute("UPDATE students SET wrong_column = 40 WHERE id = 2")

    mydb.commit()

    print("Students updated successfully!")

except mysql.connector.Error as err:
    mydb.rollback()

    print("Error:", err)
    print("Changes rolled back!")

print("\n")


# Verify rollback
try:
    mycursor.execute("SELECT * FROM students WHERE id = 1")

    result = mycursor.fetchone()

    print(result)

except mysql.connector.Error as err:
    print("Error:", err)

print("\n")


# Close connection
try:
    mycursor.close()
    mydb.close()

    print("Connection closed successfully!")

except mysql.connector.Error as err:
    print("Error closing connection:", err)
