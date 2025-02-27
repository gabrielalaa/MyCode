from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

#  The create_engine() function takes the database as one argument.
# engine = create_engine('sqlite:///:memory:', echo=True)
#  Database specific connection string !
engine = create_engine('sqlite:///mydb1.db', echo = True)
# View SQL Statements
# engine = create_engine("mysql://user:pwd@localhost/example",echo = True)

# Main Idea: : Create “SQL statement objects” instead of writing SQL. Then call its “execute” method that belongs to the object
# SQL Expression Language presents a system of representing relational database structures and expressions using Python constructs
# MetaData class from SQLAlchemy Metadata is a collection of Table objects and their associated schema constructs
meta = MetaData()

employees = Table(
   'employees', meta,
   Column('id', Integer, primary_key = True), Column('name', String),
   Column('salary', Float), Column('position', String),  Column('hiredate', String),
)

# Create the Table employees!
meta.create_all(engine)

# Insert Statements
# Prepare an insert statement
insert_statement1 = employees.insert().values(name = 'Henry', salary = '12939')
# Establish a connection to the database
connection = engine.connect()
print(insert_statement1)

# Execute multiple insert statements
# BULK Insert Statements
connection.execute(employees.insert(), [
   {'name':'Hamin', 'salary' : 5223},
   {'name':'Karin','salary' : 2323},
   {'name':'Sarin','salary' : 2311},
   {'name':'Johan','salary' : 1323},
])

# Execute the single insert statement
connection.execute(insert_statement1)

# Select all records from the employees table
s = employees.select()
result = connection.execute(s)

for row in result:
   print (row)

# connection.commit()
connection.close()