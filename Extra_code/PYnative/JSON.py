# Exercise 1

import json

data = {"key1": "value1", "key2": "value2"}

# json.dumps() for creating a json
data_json = json.dumps(data)
print(data_json)

######################################################

# Exercise 2

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2

sampleJson_dict = json.loads(sampleJson)

print(sampleJson_dict['key2'])
# value2

######################################################

# Exercise 3

import json

sampleJson = {"key1": "value1", "key2": "value2"}
# Pretty PRINT

pretty_print = json.dumps(sampleJson, indent=2, separators=(',', ' = '))
print(pretty_print)

######################################################

# Exercise 4

import json

# sort part 1
sampleJson = {"id": 1, "name": "value2", "age": 29}
# sort and convert into a dictionary
sampleJson = dict(sorted(sampleJson.items()))

# print it pretty
print(json.dumps(sampleJson, indent=2, separators=(",", " = ")))

###
# sort part 2 and create a file
sampleJson = {"id": 1, "name": "value2", "age": 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")

######################################################

# Exercise 5

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary

sampleJson_dict = json.loads(sampleJson)
print(sampleJson_dict['company']['employee']['payable']['salary'])

######################################################

# Exercise 6

import json


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format

print(json.dumps(vehicle.__dict__, indent=2, separators=(',', ' = ')))

###

from json import JSONEncoder


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)

######################################################

# Exercise 7

import json


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicle_decoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])


vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
                        object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

######################################################

# Exercise 8

import json


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)

######################################################

# Exercise 9

import json

string_json = ''' [ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]'''

# Convert it into a dictionary
string_json_dict = json.loads(string_json)

my_list = []
for i in string_json_dict:
    my_list.append(i['name'])

print(my_list)

#######

import json

sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)
