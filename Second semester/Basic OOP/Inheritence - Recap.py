class Person:
    def __init__(self, name):
        self.name = name
        self.p = None

    def pet(self, animal):
        self.p = animal
        animal.owner = self


class Pet:
    def __init__(self, owner=None):
        self.owner = owner

# Superclass / Parent class / Ancestor
class Dog(Pet):
    def __init__(self, name, color, owner=None):
        super().__init__(owner)
        self.name = name
        self.color = color

    # def bark(self):
    #         pass


# Subclass
class Husky(Dog):
    # Redefining / Overriding Methods in Subclasses

    # Additional attribute
    def __init__(self, name, color, strength, owner=None):
        # Method 1
        # Dog.__init__(self, name, color, owner)
        # Method 2
        super().__init__(name, color, owner)
        self.strength = strength

    def bark(self):
        # calling the bark method in the super class
        #         Dog.bark(self)
        print("I am ", self.name, " and I love snow")


class Cat(Pet):
    pass

class Fish(Pet):
    pass

h1 = Husky("Hus1", "white", 29)
h1.bark()

# Multiple inheritance is supported, its use is not recommended

# Is an object instance of a class?
# All huskies are dogs but not all dogs are huskies
lassie = Dog("Lassie", "black")
print(isinstance(h1,Dog))  # True
print(isinstance(lassie,Dog))  # True
print(isinstance(h1,Husky))  # True
print(isinstance(lassie,Husky))  # False

# isinstance vs issubclass
print(issubclass(Husky, Dog))  # True
print(issubclass(Dog, Husky))  # False
print(issubclass(Dog, Dog))  # True
print(issubclass(Dog, Pet))  # True
print(issubclass(Husky, Pet))  # True
print(issubclass(Person, Husky))  # False
print(issubclass(Person, Pet))  # False