class Student:
    def __init__(self, student_name, dob):
        self.student_name = student_name
        self.dob = dob

        self.uni = None
        self.exams = {}

    def takeExam(self, exam):
        grade = int(input(f"Enter a grade for {self.student_name} at {exam.exam_name} "))
        self.exams[exam.exam_name] = grade

        exam.grades.append(grade)


class University:
    def __init__(self, university_name):
        self.university_name = university_name

        self.students = []

    def enroll(self, student):
        self.students.append(student)
        student.uni = self.university_name

    def stats(self):
        for student in self.students:
            print(f"{student.student_name} took {student.exams.__len__()} exams")
            for exam, grade in student.exams.items():
                print(f"\t Got {grade} in {exam}")


class Exam:
    def __init__(self, exam_name):
        self.exam_name = exam_name

        self.grades = []

    def stats(self):
        print(f"{self.exam_name} was taken by {len(self.grades)}. Average score = {sum(self.grades)/len(self.grades)}")


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

# Task 1.3 Playing with objects
e1.stats()
e2.stats()
e3.stats()