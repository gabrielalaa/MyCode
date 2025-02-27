class Person:
    def __init__(self, name, ID):
        self.name = name
        self.id = ID

        self.__password = None

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


class University:
    def __init__(self):
        self.students = []

    def __len__(self):
        return len(self.students)


class Length:
    def __init__(self, dimension, unit):
        self.dimension = dimension
        self.unit = unit

    def __add__(self, l2):
        # Check the units first
        if self.unit == 'm':
            self.unit = 'cm'
            self.dimension = self.dimension * 100

        if self.unit == 'm':
            self.unit = 'cm'
            self.dimension = self.dimension * 100
        result = (self.dimension + l2.dimension, 'cm')
        return Length(result[0], result[1])

    def __str__(self):
        return str(self.dimension) + ' ' + str(self.unit)


# __eq__()
p1 = Person('John', 312)
p2 = Person('John', 312)

# if p1 in imc - use add to add the in

# # different ids
# print(id(p1))
# print(id(p2))
# print(p1 == p2)
# # False

# but:
print(p1 == p2)
# True

##################################

# __len__()
# THIS IS NOT A GOOD APPROACH
# Create a method in imc for adding students !!!
# This is the reason why Private and Public exist
imc = University()
imc.students.append(p1)
imc.students.append(p2)
print(len(imc.students))  # 2
# but
# print(len(imc)) does not work alone
# Because of __len__ now it works
print(len(imc))  # 2

########################################

x1 = Length(100, 'm')
x2 = Length(200, 'cm')
print(x1 + x2)

########################################

# print(p1.__password)
# SEE ON GIT WHAT HE DID HERE