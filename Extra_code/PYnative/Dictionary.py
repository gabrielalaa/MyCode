# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))
print(dictionary)
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

###

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#######################################################

# Exercise 2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

# Not that correct
dict3 = dict()

for key, value in dict1.items():
    if key in dict3:
        dict3[key].append(value)
    else:
        dict3[key] = [value]


for key, value in dict2.items():
    if key in dict3:
        dict3[key].append(value)
    else:
        dict3[key] = [value]


for key, value in dict3.items():
    if len(value) == 1:
        dict3[key] = value[0]
    else:
        if len(value) == 2 and value[0] == value[1]:
            dict3[key] = value[0]

print(dict3)

###

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

###

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

#######################################################

# Exercise 3

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

#######################################################

# Exercise 4

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dictionary = dict()
for key in employees:
    dictionary.update({key: defaults})

print(dictionary)
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

###

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

#######################################################

# Exercise 5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = dict()
for key in keys:
    new_dict[key] = sample_dict[key]

print(new_dict)
# {'name': 'Kelly', 'salary': 8000}

###

newDict = {k: sample_dict[k] for k in keys}
print(newDict)

#######################################################

# Exercise 6

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# Instead of not in I can use -
sample_dict = {k: sample_dict[k] for k in sample_dict if k not in keys}
print(sample_dict)
# {'age': 25, 'city': 'New york'}

###
# Using pop
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
# {'age': 25, 'city': 'New york'}

#######################################################

# Exercise 7

sample_dict = {'a': 100, 'b': 200, 'c': 300}

value = int(input('Enter a number: '))

if value in sample_dict.values():
    print(f"{value} is in a dict")
else:
    print(f"{value} is not in a dict")

#######################################################

# Exercise 8

sample_dict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

# Remove the key and save the value
value = sample_dict.pop('city')

sample_dict.update({'location': value})

print(sample_dict)

###

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

#######################################################

# Exercise 9

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

minimum = min(sample_dict.values())

for k in sample_dict.keys():
    if sample_dict[k] == minimum:
        print(k)
        break

###

sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#######################################################

# Exercise 10

sample_dict = {
    'emp1': {'name': 'Jon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)