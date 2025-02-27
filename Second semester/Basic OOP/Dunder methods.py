class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        # return Student(f"{self.name}+{other.name}")
        return Student(self.name + '+' + other.name)

    def __str__(self):
        return self.name


s1= Student ("Sandy") # name
s2= Student ("Spili") # name
s3= Student ("Waile") # name
print (s1+s2+s3)