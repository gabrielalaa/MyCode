class Fruit:
    pass


class Apple(Fruit):
    def __init__(self, stem_length):
        self.stem_length = stem_length


class Orange(Fruit):
    def __init__(self, pulp):
        self.pulp = pulp
        self.color = Orange


def special(list1):
    if 'apple' in list1:
        return Apple(2)
    else:
        return Orange('tasty')


# I don't know the type of x, what attributes it has, what methods...
# x = special(['apple', 'Orange'])  # -> print 2
x = special(['Apple', 'Orange'])  # -> tasty /n tasty because Apple is not apple

if isinstance(x, Apple):
    print(x.stem_length)

attrList = ['pulp', 'color']

if isinstance(x, Orange):
    print(x.pulp)

# But what happens if:
x = special(['Applr', 'Orange'])
# print(x.stem_length) # -> ERROR:
# 'Orange' obj has no attribute 'stem_length'

# if hasattr(type(x), '__iter__'):
if hasattr(x, 'pulp'):
    print(x.pulp)  # tasty

if hasattr(x, 'pulp'):
    for attr in attrList:
        setattr(x, attr, 43)
print(x.pulp)  # 43