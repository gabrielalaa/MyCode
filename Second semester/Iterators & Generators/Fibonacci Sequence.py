class FibonacciSequence:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        a, b = 0, 1  # Start with the first two numbers in the Fibonacci sequence
        count = 0
        while count < self.n:
            yield b  # Yield the next number in the sequence
            a, b = b, a + b  # Update a and b to the next two numbers
            count += 1

# Example of using next() manually
fib = FibonacciSequence(10)
fib_iter = iter(fib)
print(next(fib_iter))  # Output: 1
print(next(fib_iter))  # Output: 1
print(next(fib_iter))  # Output: 2

# Example of using a for loop
for number in FibonacciSequence(10):
    print(number)