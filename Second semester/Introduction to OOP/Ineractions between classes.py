# Left part view
class Dog:
    def __init__(self, name):
        self.name = name

        # I only know that those exist
        self.color = None
        self.owner = None


class Person:
    def __init__(self, name):
        self.name = name

        self.age = None


p = Person("Mr Smith")
d = Dog("Lassie")

# OBJECT DIAGRAM
# The value is a reference to other object
d.owner = p

print(p.name)
# Mr Smith
print(d.owner.name)
# Mr Smith