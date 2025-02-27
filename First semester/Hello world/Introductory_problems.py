# Task 1 Fahrenheit to Centigrade
f_temperature = 45
c = (f_temperature - 32) * 5 / 9
print("Temperature is", f_temperature)

# Task 2 Miles to Kilometers
var_miles = 4
var_kilometers = var_miles * 1.6
print("Kilometers are", var_kilometers)

# Task 3 Celsius to Fahrenheit
c_temp = 11
f = c_temp * (9/5) + 32
print("Fahrenheit is", f)

# Task 4 CountingApples
money = int(input("Enter your money: "))
print(f"You can buy {money//3} apples.")
print(f"You need {3 - money % 3 } for one more apple")

# Import math Library
import math
# Print the value of pi
print(math.pi)

# Task 5 Area of a circle
r = float(input("Input the radius of the circle : "))
print(f"The radius of the circle is {r}")
# Area of the circle
A = math.pi * r ** 2
rounded_A = round(A, 2)
print(f"The Area is {rounded_A}")

# Task 6 Volume of a cylinder
r = float(input("Input the radius of the cylinder: "))
print(f"The radius of the cylinder is {r}")
h = float(input("Input the height of the cylinder: "))
print(f"The height of the cylinder is {h}")
# Calculate the volume
V = math.pi * r ** 2 * h
rounded_V = round(V, 2)
print(rounded_V)

# Task 7 Sum of numbers
x = float(input("Please, input your first number: "))
y = float(input("Please, input your second number: "))
sum = x + y
print(f"The sum of your numbers is {sum}. Thank you !")

# Task 8 Number Formats
num = int(input("Your Decimal number is: "))
print(f"Your conversion is {oct(num)}")

# Task 9 Base and Exponents
base = int(input("Input base: "))
exponent = int(input("Input exponent: "))
print(f"base = {base}\nexponent = {exponent}\n{base} raises to the power of {exponent} is: {base ** exponent}")