class Person:
    def __init__(self, name):
        self.name = name
        self.animal = None

    def pet(self, animal):
        self.animal = animal
        animal.owner = self


class Pet:
    def __init__(self, name, owner=None, home=None):
        self.name = name
        self.owner = owner
        self.home = home

    def livesIn(self, place):
        self.home = place
        # Add the pet to the appropriate list in the place object
        if isinstance(self, Dog):
            place.dogs.append(self)
        elif isinstance(self, Cat):
            place.cats.append(self)
        elif isinstance(self, Fish):
            place.fishs.append(self)


class Dog(Pet):
    def __init__(self, name, owner=None, home=None):
        super().__init__(name, owner, home)
        # self.home = home


class Husky(Dog):
    def __init__(self, age, name, home=None, owner=None):
        super().__init__(name, owner, home)
        self.age = age


class Kennel:
    def __init__(self, location):
        self.location = location
        self.dogs = []


class Cat(Pet):
    def __init__(self, color, name, owner=None, home=None):
        super().__init__(name, owner, home)
        self.color = color
        # self.home = home


class CatHouse:
    def __init__(self, location):
        self.location = location
        self.cats = []


class Fish(Pet):
    def __init__(self, name, home=None, owner=None):
        super().__init__(name, owner, home)
        # self.home = home


class Aquarium:
    def __init__(self, location):
        self.location = location
        self.fishs = []
