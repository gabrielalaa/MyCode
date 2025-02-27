import pickle

class HelperObject:
    pass

class Person :

    def __init__(self, name, age ):
        self. name = name
        self. age = age
        self.connected = None

    def showInfo (self):
        return "Person with name " + self.name + " and age " + str (self.age) + " is connected to " + str (self.connected)

    def connectPeople (self, person):
        self.connected = person
        person.connected = self

    def __str__(self):
        return self.name + str (self.age)



p1 = Person ("Manuel", 32)
p2 = Person ("Samuel", 45)
print (p1.showInfo())
p1.connectPeople(p2)
print (p2.showInfo())

#with open ("person-data", "wb") as obfile :
    #pickle.dump (p1, obfile)

with open ("person-data", "rb") as datafile:
    p = pickle.load (datafile)
    print (type(p))
    print (p.showInfo())
