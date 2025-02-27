# Exercise 1

def function(name, age):
    print(name, age)


name = 'Gabriela'
age = 20
function(name, age)


#######################################################

# Exercise 2

def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)

#######################################################

# Exercise 3


def calculation(a, b):
    # Your Code
    return a + b, a - b


res = calculation(40, 10)
print(*res)

#######################################################

# Exercise 4


def showEmployee(name, salary = 9000):
    print(f"Name: {name} salary: {salary}")


showEmployee("Ben", 12000)
showEmployee("Jessa")

#######################################################

# Exercise 5


def outer(a, b):
    def inner(a1, b1):
        return a1 + b1
    return inner(a, b) + 5


print(outer(5, 5))

#######################################################

# Exercise 6


def recursive(number):
    if number == 0:
        return 0
    # elif number == 1:
    #     return 1
    else:
        return number + recursive(number - 1)


print(recursive(10))


#######################################################

# Exercise 7

def display_student(name, age):
    print(name, age)


# call using original name
display_student("Emma", 26)

# display_student = show_student = lambda name, age: print(name, age)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

#######################################################

# Exercise 8


def even(n, m):
    # Method 1
    # my_list = list((element for element in range(n, m) if element % 2 == 0))
    # return my_list

    # Method 2
    return list(range(n, m, 2))


print(even(4, 30))


#######################################################

# Exercise 9


def largest_number(l):
    return max(l)


x = [4, 6, 8, 24, 12, 2]
print(largest_number(x))
