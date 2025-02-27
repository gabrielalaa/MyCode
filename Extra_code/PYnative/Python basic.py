# Exercise 1

a, b = int(input('Enter a: ')), int(input('Enter b: '))
if a*b < 1000:
    print(f'The the result is {a*b}')
else:
    print(f'The result is {a+b}')

#######################################################

# Exercise 2

for i in range (10):
    print(f'Current Number {i} Previous Number {i-1} Sum {i+i-1}')

#######################################################

# Exercise 3

string = input("Enter: ")
print(f'Original string: {string}')
print('Printing only even index chars')
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])

#######################################################

# Exercise 4

def remove_first_n(string, char):
    return string[char:]


print(remove_first_n('pynative', 4))
print(remove_first_n('pynative', 2))

#######################################################

# Exercise 5

def first_and_last (l):
    if l[0] == l[-1]:
        return True
    return False


print(first_and_last([10, 20, 30, 40, 10]))
print(first_and_last([75, 65, 35, 75, 30]))

#######################################################

# Exercise 6

given_list = [10, 20, 33, 46, 55]
print('Divisible by 5')
for i in given_list:
    if i % 5 == 0:
        print(i)

#######################################################

# Exercise 7

str_x = "Emma is good developer. Emma is a writer"
print(str_x.count('Emma'))

#######################################################

# Exercise 8

for num in range(6):
    print(' '.join(str(num)*num))

#######################################################

# Exercise 9

def check_palindrome (number):
    if str(number) == str(number)[::-1]:
        return True
    return False

print(check_palindrome(121))
print(check_palindrome(125))

#######################################################

# Exercise 10

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
l1 = [i for i in list1 if i % 2 != 0]
l2 = [i for i in list2 if i % 2 == 0]
print(l1+l2) # [25, 35, 40, 60, 90]

#######################################################

# Exercise 11

def extract_digits(number):
    string = str(number)
    return " ".join(string[::-1])


print(extract_digits(7536))

#######################################################

# Exercise 12

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

#######################################################

# Exercise 13

for i in range(1, 11):
    print(i, end="  ")
    for j in range(1, 11):
        print(i*j, end=" ")
    print()

#######################################################

# Exercise 14

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print('*', end=' ')
    print(' ')


#######################################################

# Exercise 15

b = int(input("Enter "))
e = int(input("Enter "))
def exponent(base, exp):
    return base ** exp
result = exponent(b, e)
print(f'{b} raises to the power of {e}: {result}')