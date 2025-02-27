import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('mydb1.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table named 'employees' if it doesn't already exist
cursor.execute(
	"""CREATE TABLE if not exists employees(
                  id integer PRIMARY KEY, 
                  name text, 
                  salary real, 
                  department text, 
                  position text, 
                  hireDate text)"""
	)

# Inserting data into the table (commented out, but can be used to add records)
cursor.execute("INSERT INTO employees VALUES(14, 'John4', 2700, 'IT', 'Manager', '2019-01-07')")
#cursor.execute("INSERT INTO employees VALUES(24, 'Jane4', 4700, 'HR', 'Manager', '2007-04-06')")

# Query a Database
# Ask user for minimum salary
salary = input ("Enter min. salary")

# Placeholder, Value (Tuple)
# cursorObj.execute('SELECT * FROM employees WHERE name=?', (name,))
# Placeholder, Value (Dict)
# cursorObj.execute('SELECT * FROM employees WHERE name=:n',{"n": name})

# WARNING: The next line is vulnerable to SQL Injection attacks
# This line directly inserts the user input into the SQL query
cursor.execute('select * from employees where position="Manager" and salary>'+salary)  # NEVER do this +salary | Prone to SQL Injection
# cursorObj.execute('SELECT * FROM employees WHERE name={}’.format(name))  # NEVER do this +salary | Prone to SQL Injection

# Consider:
# cursor.execute('SELECT * FROM employees WHERE position="Manager" AND salary>' + salary)
# Of the user inputs:
# 0; DROP TABLE employees
# The SQL query becomes
# SELECT * FROM employees WHERE position="Manager" AND salary>0; DROP TABLE employees;
# Selects all employees with the position "Manager" and a salary greater than 0.
# Deletes the entire employees table (DROP TABLE employees), causing data loss.
# Corrected Version to Avoid SQL Injection
# # Use parameterized query to safely insert user input
# cursor.execute('SELECT * FROM employees WHERE position=? AND salary>?', ("Manager", salary))
# By using placeholders (?), you ensure that user input is treated as data, not as part of the SQL command, thereby preventing SQL injection attacks.

# Fetch all results from the last executed query
all_rows = cursor.fetchall()

# Iterate over and print all fetched rows
for row in all_rows:
	print (row)

# Commit the changes to the database (useful when modifying data)
connection.commit()

# Close the connection to the database
connection.close()