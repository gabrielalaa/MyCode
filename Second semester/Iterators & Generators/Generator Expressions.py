# List Comprehension
print(sum([x*x for x in range(10)]))

# Generator Expression
print(sum(x*x for x in range(10)))

# Especially useful with functions like sum(), min(), and max() that reduce an iterable input to a single value
print(max(len(line) for line in file if line.strip()))