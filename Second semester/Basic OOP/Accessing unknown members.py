class Student:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def get_age(self):
        return self.age

    def __str__(self):
        return self.age


f = Student("Bob Smith", 23)
print(getattr(f, "full_name"))
print(getattr(f, "get_age"))
# getattr(f, 'get_age')() # call it
# getattr(f, 'get_birthday')# Raises AttributeError – No method!