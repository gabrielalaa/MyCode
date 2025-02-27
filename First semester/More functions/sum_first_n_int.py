# Write a recursive Python function that returns the sum of the first n integers

def calculate_sum(n):
    if n == 1:
        return n
    else:
        return n + calculate_sum(n-1)


number = int(input("Enter a number: "))
print(f"The sum of the first {number} integers is {calculate_sum(number)}")