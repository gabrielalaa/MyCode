class Student:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __str__(self):
        return f'{self.name}. DOB: {self.dob}'


s1 = Student("Sandy", "24.01.1992")  # name, dob
s2 = Student("Spili", "14.10.1993")  # name, dob
s3 = Student("Waile", "04.06.1994")  # name, dob

for s in (s1, s2, s3):
    print(s)