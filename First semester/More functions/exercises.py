#  Task 1
def base_exp(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * base_exp(base, exp - 1)


print(base_exp(2, 4))
print(base_exp(3, 3))


###################################################################

# Task 2
def sum_of_digits(number):
    # Base case: if the number has only one digit
    if number < 10:
        return number
    else:
        # Otherwise, return the sum of the last digit and recurse the number without it
        return number % 10 + sum_of_digits(number // 10)


print(sum_of_digits(345))
print(sum_of_digits(49))
print(sum_of_digits(7))


###################################################################

# Task 3
def print_numbers(n):
    if n == 0:
        print(0)
    else:
        # Print the current number
        print(n)
        print_numbers(n - 1)


print_numbers(10)


###################################################################

# Task 4
def find_youngest_and_oldest(students):
    # Use the min and max functions with a key argument that specifies to compare by 'age'
    youngest = min(students, key=lambda x: x['age'])
    oldest = max(students, key=lambda x: x['age'])
    # Return a tuple with the names of the youngest and oldest students
    return (youngest['name'], oldest['name'])


# Example usage of the function with a list of student dictionaries
students_list = [
    {"name": "Saint", "age": 25},
    {"name": "Watson", "age": 35},
    {"name": "Karlson", "age": 21},
    {"name": "Kenzo", "age": 15},
    {"name": "Kylie", "age": 19},
    {"name": "Elijah", "age": 20},
    {"name": "Mason", "age": 21},
    {"name": "Logan", "age": 21},
    {"name": "James", "age": 24},
    {"name": "Oliver", "age": 21},
    {"name": "Liam", "age": 24}
]

youngest_oldest = find_youngest_and_oldest(students_list)
print("Youngest student:", youngest_oldest[0])
print("Oldest student:", youngest_oldest[1])


###

def min_max(l):
    # returns (y, o)
    # y = name of the youngest student
    # o = name of the oldest student

    # Find the dict for each student
    y_d = min(students, key=lambda student: student['age'])
    o_d = max(students, key=lambda student: student['age'])
    # print(y)
    # {'name': 'Kenzo', 'age': '15'}

    # Save the names
    y = y_d['name']
    o = o_d['name']

    return y, o


students = [{"name": "Saint", "age": "25"},
            {"name": "Watson", "age": "35"},
            {"name": "Karlson", "age": "21"},
            {"name": "Kenzo", "age": "15"},
            {"name": "Kylie", "age": "19"},
            {"name": "Elijah", "age": "20"},
            {"name": "Mason", "age": "21"},
            {"name": "Logan", "age": "21"},
            {"name": "James", "age": "24"},
            {"name": "Oliver", "age": "21"},
            {"name": "Liam", "age": "24"}]

print(min_max(students))


###################################################################

#  Task 5
def coordinates(p):
    # Sort the list of coordinates based on the second element of the tuple (y-axis)
    return sorted(p, key=lambda x: x[1])


points = [(12, 3), (4, 3), (6, 5), (3, 8),
          (42, 3), (2, 7), (1, 0), (3, 4),
          (15, 6), (3, 7), (5, 9), (8, 8),
          (12, 2), (4, 2), (6, 5), (3, 4),
          (15, 3), (4, 6), (6, 3), (3, 8)]

print(coordinates(points))

###################################################################

# Task 6

from math import sqrt


def sort_by_distance_from_origin(points):
    # Define a function to calculate the distance from the origin
    def distance_from_origin(point):
        # Distance formula from origin is sqrt(x^2 + y^2)
        return math.sqrt(point[0] ** 2 + point[1] ** 2)

    # Sort the list of coordinates based on the distance from the origin
    return sorted(points, key=distance_from_origin)


# Example usage of the function with a list of coordinates
example_points = [(1, 2), (3, 4), (0, 0), (-1, -1), (2, -3), (-2, 2)]

# Call the sorting function
sorted_points_by_distance = sort_by_distance_from_origin(example_points)


###################################################################

#  Task 7

def sort_students_by_age(students):
    # Sort the list of students based on the 'age' key
    return sorted(students, key=lambda student: student['age'])


# Example usage of the function with a list of student dictionaries
students_list = [
    {"name": "Saint", "age": 25},
    {"name": "Watson", "age": 35},
    {"name": "Karlson", "age": 21},
    {"name": "Kenzo", "age": 15},
    {"name": "Kylie", "age": 19},
    {"name": "Elijah", "age": 20},
    {"name": "Mason", "age": 21},
    {"name": "Logan", "age": 21},
    {"name": "James", "age": 24},
    {"name": "Oliver", "age": 21},
    {"name": "Liam", "age": 24}
]

sorted_students_by_age = sort_students_by_age(students_list)
print(sorted_students_by_age)

###################################################################

#  Task 8
import math


def calculate_distance(point):
    x, y, z = point
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)


# List of 3D points
points = [(12, 21, 2), (12, 5, 4), (12, 75, 3)]

# Use the map function to apply the distance calculation to each point
distances = list(map(calculate_distance, points))


###################################################################

#  Task 9
def sorted_names(s):
    # Sort the list
    new = sorted(s, key=lambda x: x['age'])
    # Return only the names
    return list(map(lambda x: x['name'], new))


students_list = [
    {"name": "Saint", "age": 25},
    {"name": "Watson", "age": 35},
    {"name": "Karlson", "age": 21},
    {"name": "Kenzo", "age": 15},
    {"name": "Kylie", "age": 19},
    {"name": "Elijah", "age": 20},
    {"name": "Mason", "age": 21},
    {"name": "Logan", "age": 21},
    {"name": "James", "age": 24},
    {"name": "Oliver", "age": 21},
    {"name": "Liam", "age": 24}
]

print(sorted_names(students_list))


###################################################################

#  Task 10
def filterbyAgeSex(listS, sex, age):
    # for the given sex
    # filter based on age > given age

    # Filter the list based on wanted sex
    new = list(filter(lambda x: x['sex'] == sex, listS))
    # Filter and return the list based on the condition for the wanted age
    return list(filter(lambda x: x['age'] > age, new))


students = [{"name": "Sai", "age": 25, "sex": 'F'},
            {"name": "Wat", "age": 35, "sex": 'F'},
            {"name": "Kar", "age": 21, "sex": 'F'},
            {"name": "Ken", "age": 15, "sex": 'M'},
            {"name": "Kyl", "age": 19, "sex": 'F'},
            {"name": "Eli", "age": 20, "sex": 'F'},
            {"name": "Mas", "age": 21, "sex": 'M'},
            {"name": "Log", "age": 21, "sex": 'F'},
            {"name": "Jam", "age": 24, "sex": 'M'},
            {"name": "Oli", "age": 21, "sex": 'M'},
            {"name": "Lia", "age": 24, "sex": 'F'}]

print(list(filterbyAgeSex(students, "M", 12)))
print(list(filterbyAgeSex(students, "F", 30)))
# [{'name': 'Ken', 'age': 15, 'sex': 'M'}, {'name': 'Mas', 'age': 21, 'sex': 'M'}, {'name': 'Jam', 'age': 24,
# 'sex': 'M'}, {'name': 'Oli', 'age': 21, 'sex': 'M'}] [{'name': 'Wat', 'age': 35, 'sex': 'F'}]