# Method I
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # using list comprehensions
    output = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(output)

###################################################

# Method II
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # the final list
    all_permutations = []
    # the permutations
    ijk = []
    # using for loops
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    ijk = [i, j, k]
                    all_permutations.append(ijk)
    print(all_permutations)