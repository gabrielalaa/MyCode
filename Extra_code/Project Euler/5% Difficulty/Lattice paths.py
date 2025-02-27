def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def lattice_paths(grid):
    a = factorial(grid * 2)
    b = factorial(grid)
    return a // (b * b)


print(lattice_paths(20))
