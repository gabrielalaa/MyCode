# How we create objects
class Dog:
    # We define a function inside the class Dog

    # self - reference to the object; behave like it already exists; ignores it
    # self - has to be inside an object to mean something
    # a convention; you can use other name but don't

    # when a function init is called, python knows the object is not yet created

    # the order of a function it doesn't matter

    # CONSTRUCTOR
    def __init__(self, name, color):
        # print(self)
        # <__main__.Dog object at 0x0000029F531EFAC0

        # print("Hello", name)
        # Hello Lassie
        # Hello Rocky

        # name = name will disappear
        # use self.
        self.name = name
        self.color = color

        # we can have
        self.bark()

        # If we create a self.age = 10 here, and we use it in bark function, it doesn't exist anymore

    # METHOD
    def bark(self):
        print(f"{self.name} is barking")

    # pass


# self is lassie
# INSTANTIATION
lassie = Dog("Lassie", "black")

lassie.bark()
# Lassie is barking

lassie.name = "Junky"
print(lassie.name)
# Junky

lassie.bark()
# Junky is barking

print(lassie.color)
# black

#####################

# self is rocky
# INSTANTIATION
rocky = Dog("Rocky", "white")

carly = Dog("Carly", "red")

# print(lassie)

########################################################


# class Person:
#     pass
#
#
# deepak = Person()
# sam = Person()