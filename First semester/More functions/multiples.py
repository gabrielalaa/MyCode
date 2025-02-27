# Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3.
def multiples(m, number):
    # Base case: If n is one, return the first multiple
    if number == 1:
        return m
    else:
        return multiples(m, number - 1) + m


# Take input

mult_of_ = int(input("Enter the number you want to find multiples of:  "))
n = int(input("How many: "))
print(multiples(mult_of_, n))