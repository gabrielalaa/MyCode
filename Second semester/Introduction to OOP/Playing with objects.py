class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def noise(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def birthday(self):
        print(f"{self.name} was born in {2024-self.age}")


class Person:
    def __init__(self, name):
        self.name = name

    def feed(self, a, food):
        print(f"{self.name} just fed {a.name}: {food}")


animals = [
    Animal("Tiger32", 12, 121),
    Animal("Lion42", 4, 131),
    Animal("Zebra 12", 12, 11),
    Animal("Bison 23", 4, 121),
    # add more
]

caretaker = Person("Joe")
for animal in animals:
    caretaker.feed(animal, "Apple")

for animal in animals:
    animal.birthday()