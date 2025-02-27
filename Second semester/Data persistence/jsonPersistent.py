import json


class Person :

    def __init__(self, name, age ):
        self. name = name
        self. age = age
        self.connected = None

    def showInfo (self):
        return "Person with name " + self.name + " and age " + str (self.age) + " is connected to " + str (self.connected)

    def connectPeople (self, person):
        self.connected = person

    # def __str__(self):
    #     return self.name + str (self.age)


class PersonDecoder (json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.person_converter, *args, **kwargs)

    def person_converter (self, jsonstring):
        print ("Got this to convert " + str(jsonstring))
        p = Person (jsonstring["name"], jsonstring["age"])
        return p



p1 = Person ("Manuel", 32)
p2 = Person ("Samuel", 45)
print (p1.showInfo())
p1.connectPeople(p2)

jsonString = json.dumps(p1, default=lambda o: o.__dict__)

print ("JSON String is ", jsonString)

x = json.loads(jsonString, cls = PersonDecoder)

print (type(x))
