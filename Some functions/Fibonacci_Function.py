def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  # the seventh element

##################################################

# Fibonacci numbers:
# 0 1 1 2 3 5 8 13 21 34

# first two numbers
num1, num2 = 0, 1

print("Fibonacci numbers: ")
# run loop 10 times
for i in range(10):
    print(num1, end=" ")
    # add last two numbers to get next number
    num3 = num1 + num2

    # update values
    num1 = num2
    num2 = num3

# or

# Print the n fibo numbers
def fibonacci(n):
    # first element
    n1 = 0
    # second element
    n2 = 1
    # third element
    n3 = 1

    fibo_numbers = []
    for i in range(n):
        # Add the first element
        fibo_numbers.append(n1)
        n1 = n2
        n2 = n3
        n3 = n1 + n2
    return ' '.join([str(i) for i in fibo_numbers])


print(fibonacci(10))


##################################################

# using arrays

# creating an array in the function to find the
# nth number in fibonacci series. [0, 1, 1, ...]
def fibonacci(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]


# Driver Program
print(fibonacci(9))

###############################################

# Check if a number is a fibonacci number or not

n = int(input("Enter the number: "))
c = 0
a = 1
b = 1
if n == 0 or n == 1:
    print("Yes")
else:
    while c < n:
        c = a + b
        b = a
        a = c
    if c == n:
        print("Yes")
    else:
        print("No")


###

# Check if a number is fibo or not
def fibonacci(n):
    if n == 0 or n == 1:
        return True
    else:
        a = 0
        b = 1
        c = 1
        while c < n:
            c = a + b
            a, b = b, c
            if c == n:
                return True
    return False


print(fibonacci(1))
print(fibonacci(8))
print(fibonacci(10))
print(fibonacci(377))
print(fibonacci(609))
