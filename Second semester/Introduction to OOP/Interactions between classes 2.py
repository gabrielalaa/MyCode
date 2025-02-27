
class Dog:
    def __init__(self, name):
        self.name = name

        # I only know that those exist
        self.color = None
        self.owner = None

    # def set_owner(self, person):
    #     pass


class Person:
    def __init__(self, name):
        self.name = name

        self.age = None
        self.pet = None

    def set_pet(self, d1):
        self.pet = d1
        d1.owner = self


p = Person("Mr Smith")
d = Dog("Lassie")

# OBJECT DIAGRAM
# The value is a reference to the other object
# Risky
# d.owner = p
# p.pet = d

p.set_pet(d)

print(p.name)
# Mr Smith
print(d.owner.name)
# Mr Smith