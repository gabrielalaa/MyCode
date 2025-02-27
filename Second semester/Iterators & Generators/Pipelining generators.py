# Multiple generators can be used to pipeline a series of operations
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

# a generator which takes another generator
print(sum (square (fibonacci_numbers(10))))
# We don't care about the data type but rather if it is iterable