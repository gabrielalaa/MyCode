# Define each class
# from collections import Counter

class Student:
    # CONSTRUCTOR
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

        # We know it exists
        # enroll
        self.e = None

        # exam
        self.exa = None
        # self.Counter = Counter()
        self.li = []
        self.grade = None

    # METHOD for taking the exam
    def takeExam(self, ex):
        self.exa = ex
        ex.exa = self
        self.grade = int(input(f"Enter your grade for {self.name} at {self.exa.course}: "))
        # self.Counter.update(self.exa)
        self.li.append(f"Got {self.grade} in {self.exa.course}")


class Exam:
    # CONSTRUCTOR
    def __init__(self, course):
        self.course = course

        # Exam
        self.exa = None


class University:
    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name

        # enroll
        self.s = None

        # statistics
        self.l = None

    # METHOD of enrolling a student
    def enroll(self, st):
        self.s = st
        st.e = self
        # EXTRA
        print(f"{self.s.name} is enrolled")

    # METHOD of statistics
    def stats(self):
        print(f'{s1.name} took {len(s1.li)} exams')
        for exam in s1.li:
            print(f"\t\t\t {exam}")

        print(f'{s2.name} took {len(s2.li)} exams')
        for exam in s2.li:
            print(f"\t\t\t {exam}")

        print(f'{s3.name} took {len(s3.li)} exams')
        for exam in s3.li:
            print(f"\t\t\t {exam}")


# INSTANTIATION
s1 = Student("Sandy", "24.01.1992")  # name, dob
s2 = Student("Spili", "14.10.1993")  # name, dob
s3 = Student("Waile", "04.06.1994")  # name, dob

imc = University("FH Krems")

imc.enroll(s1)
imc.enroll(s2)
imc.enroll(s3)

e1 = Exam("Programming II")
e2 = Exam("Software Eng")
e3 = Exam("Creativity")

# assign a random value as grade
s1.takeExam(e1)
s2.takeExam(e1)
s3.takeExam(e1)

s1.takeExam(e2)
s2.takeExam(e2)

s1.takeExam(e3)
s3.takeExam(e3)

# print(f'{s1.name} took {len(s1.li)} exams')
# for exam in s1.li:
#     print(f"\t\t\t {exam}")
#
# print(f'{s2.name} took {len(s2.li)} exams')
# for exam in s2.li:
#     print(f"\t\t\t {exam}")
#
# print(f'{s3.name} took {len(s3.li)} exams')
# for exam in s3.li:
#     print(f"\t\t\t {exam}")

imc.stats()