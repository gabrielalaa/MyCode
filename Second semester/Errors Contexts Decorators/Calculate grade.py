# Calculate the average grade for a student
# Custom exception if invalid

class InvalidGradeException(Exception):
    pass

def calculate_grade(grades_list):
    number_grades = len(grades_list)
    s = 0

    for grade in grades_list:
        if grade < 0 or grade > 100:
            raise InvalidGradeException("Invalid grade encountered! Grades should be between 0 and 100")
        else:
            s += grade

    return s / number_grades

grades = list(map(int, input('Enter the grades separated by commas ').strip().split(',')))

try:
    print(calculate_grade(grades))
except InvalidGradeException as e:
    print(e)