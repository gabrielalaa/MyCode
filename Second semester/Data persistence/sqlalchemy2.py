from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base Class
Base = declarative_base()

class Employee(Base):
   __tablename__ = 'employees'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   salary = Column(Float)
   email = Column(String)
   def __init__(self):
       pass
   #def...

engine = create_engine('sqlite:///mydb2.db', echo = True)

Base.metadata.create_all(engine)



SessionClass = sessionmaker(bind = engine)
session= SessionClass()


e1 = Employee ()
e2 = Employee ()
e2.salary = 4999

e1.email = "happy@gmail.com"
e1.name = "Happy Birthday"

session.add(e1)
session.add(e2)

session.commit()