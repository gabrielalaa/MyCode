class Student:
    # CONSTRUCTOR
    def __init__(self, name, dob):
        self.student_name = name
        self.dob = dob

        # We only know about their existence:
        self.enroll_uni = None
        self.take_exam = None
        self.grade = None

        # Create a list for each student's performance
        self.marks = []

    # Create a METHOD for taking an exam
    def takeExam(self, exam):
        self.take_exam = exam
        exam.student_take_exam = self
        self.grade = int(input(f"Enter your grade for {self.student_name} at {self.take_exam.exam_name}: "))
        self.marks.append(f"Got {self.grade} in {self.take_exam.exam_name}")


class University:
    def __init__(self, name):
        self.uni_name = name

        self.enroll_student = None

        # Create a list for enrolled students
        self.enrolled_students = []

    # Create a method for enroll
    def enroll(self, student):
        self.enroll_student = student
        student.enroll_uni = self
        print(f"Enrolling {self.enroll_student.student_name} at {self.uni_name}")
        self.enrolled_students.append(student)

    # Create a method for statistics
    def stats(self):
        for student in self.enrolled_students:
            print(f"{student.student_name} took {len(student.marks)} exams")
            for s in student.marks:
                print(f"\t\t {s}")


class Exam:
    def __init__(self, name):
        self.exam_name = name

        self.student_take_exam = None

    #     self.university = None
    #
    # def assign_uni(self, uni):
    #     self.university = uni

    # Create method for statistics
    def stats(self):
        # Create a dictionary to store the grades for each course
        grades = dict()

        # For each enrolled student
        for student in imc.enrolled_students:
            # In each performance
            for performance in student.marks:
                # Extract the name of the course and the grade
                # Got {self.grade} in {self.take_exam.exam_name}
                grade, course = performance.split(' in ')
                grade = int(grade.replace('Got ', ''))

                if course not in grades:
                    grades[course] = []
                grades[course].append(grade)

        # If the exam is in the dictionary, print the performance
        if self.exam_name in grades:
            average = sum(grades[self.exam_name]) / len(grades[self.exam_name])
            print(f"{self.exam_name} was taken by {len(grades[self.exam_name])}. Average score = {average}")


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

# print statistics
imc.stats()

e1.stats()
e2.stats()
e3.stats()