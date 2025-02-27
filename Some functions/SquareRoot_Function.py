# Method I
def square_root(x):
    return x ** 0.5


number = int(input("Enter:"))
number = square_root(number)
number = round(number, 2)  # 2 optional
print(number)

##################################################

# Method II
s_r = lambda y: y ** 0.5

##################################################

# Method III
from math import sqrt

print(sqrt(2))
