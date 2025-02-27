import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.connected = None

    def showInfo(self):
        return "Person with name " + self.name + " and age " + str(self.age) + " is connected to " + str(self.connected)

    def connectPeople(self, person):
        self.connected = person

    # def __str__(self):
    #     return self.name + str(self.age)

# Create instances of Person
p1 = Person("Manuel", 32)
p2 = Person("Samuel", 45)
print(p1.showInfo())
p1.connectPeople(p2)

# Serialize Person object to JSON using lambda function
jsonString = json.dumps(p1, default=lambda o: o.__dict__)
print("JSON String is", jsonString)

# Deserialize JSON back to Person object using lambda function
x = json.loads(jsonString, object_hook=lambda d: Person(d['name'], d['age']))
print(f"Decoded Person: {x.showInfo()}")