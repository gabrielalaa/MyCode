# We don't have to define them multiple times

class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def speak(self):
        print(f'Hello my name is {self.name}')


class Teacher(Person):
    def __init__(self, name, address, age, salary):
        # MUST BE THE FIRST LINE:
        Person.__init__(self, name, address, age)
        self.salary = salary

    def speak(self):
        # If you want to print firstly what is included in the SUPERCLASS:
        # always use super(). first
        super().speak()
        # or
        Person.speak(self)
        print(f'Hello my name is {self.name} and I live in {self.address}')


class Student(Person):
    def __init__(self, name, address, age, study_prog):
        # MUST BE THE FIRST LINE:
        # it also exists super
        Person.__init__(self, name, address, age)
        self.study_prog = study_prog

        self.fees = None

    def __str__(self):
        return f'{self.name} lives in {self.address}, and she is studying {self.study_prog} at the age of{self.age}'

    def speak(self):
        print(f'Hello my name is {self.name} and I study {self.study_prog}')


class EUStudent(Student):
    def __init__(self, name, address, age, study_prog):
        super().__init__(name, address, age, study_prog)
        self.fees = 300


class NonEUStudent(Student):
    def __init__(self, name, address, age, study_prog):
        super().__init__(name, address, age, study_prog)
        self.fees = 800


s1 = Student('Gabriela', 'Krems', 20, 'Programming')
print(s1)
# Error at first
# Variables exists only if they are executed first
# We have to create them first!
# TO RUN THE CONSTRUCTOR OF class Person
s1.speak()
# Hello my name is Gabriela

# print(repr(s1))

print()

t1 = Teacher('Deepak D', 'Krems', '30', 1000)
print(f'Teacher {t1.name} earns {t1.salary} $')
t1.speak()

print()

s2 = EUStudent('Jack', 'Krems', 24, 'Programming')
print(f'Student {s2.name} is paying {s2.fees} $')

s3 = NonEUStudent('Mark', 'Viena', 22, 'Programming')
print(f'Student {s3.name} is paying {s3.fees} $')