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

    def stats(self):
        # Create a dictionary to store grades for each course
        course_grades = dict()

        # Loop through all students enrolled
        for student in imc.students:
            for g in student.li:
                # Extract the grade and course from the string I have in my list
                grade_text, course = g.split(' in ')
                grade = int(grade_text.replace('Got ', ''))

                # Add the grade to the list for each course
                if course not in course_grades:
                    course_grades[course] = []
                course_grades[course].append(grade)

        # Print
        if self.course in course_grades:
            average_g = sum(course_grades[self.course])/len(course_grades[self.course])
            print(f"{self.course} exam was taken by {len(course_grades[self.course])} students Average score = {average_g}")

        # for course, grades in course_grades.items():
        #     average_g = sum(grades) / len(grades)
        #     print(f"{course} exam was taken by {len(grades)} students Average score = {average_g}")


class University:
    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name

        # enroll
        self.s = None

        # statistics
        self.l = None

        # list of students enrolled
        self.students = []

    # METHOD of enrolling a student
    def enroll(self, st):
        self.s = st
        st.e = self
        # EXTRA
        print(f"{self.s.name} is enrolled")
        self.students.append(self.s)

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


imc.stats()

e1.stats()
e2.stats()
e3.stats()