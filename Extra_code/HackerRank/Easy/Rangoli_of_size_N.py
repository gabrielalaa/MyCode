# Correct version
def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


###########################################################

# First attempt
def print_rangoli(size):
    # create a list of letters that will be used
    list_of_letters = []
    for i in range(size):
        list_of_letters.append(chr(ord('a')+i))
    list_of_letters.reverse()
    # or
    # list_of_letters = [chr(ord('a') + i) for i in range(size)]
    # list_of_letters.reverse()

    # determine the width of the rangoli
    # based on what I see below, the formula
    # for the width = n * 4 - 3
    width = n * 4 - 3

    # create the rangoli pattern
    # I can use join method for this
    for i in range(size):
        # create the left side
        left_side = '-'.join(list_of_letters[:i+1])

        # print(left_side)
        # e
        # e-d
        # e-d-c
        # e-d-c-b
        # e-d-c-b-a

        # create the right side
        right_side = '-'.join(list_of_letters[:i][::-1])

        # print(right_side)
        # e
        #
        # e-d
        # e
        # e-d-c
        # d-e
        # e-d-c-b
        # c-d-e
        # e-d-c-b-a
        # b-c-d-e

        # create the entire row
        row = left_side + '-' + right_side
        print(row.center(width, '-'))

    # Create the lower part - which is the reverse of the upper half
    for i in range(size-2, -1, -1):
        left_side = '-'.join(list_of_letters[:i+1])
        right_side = '-'.join(list_of_letters[:i][::-1])
        row = left_side + '-' + right_side
        print(row.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# # for size 10 -> 37
# print(len('j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j'))
# # for size 5 -> 17
# print(len('e-d-c-b-a-b-c-d-e'))
# # for size 3 -> 9
# print(len('c-b-a-b-c'))

###########################################################

# Second attempt

def print_rangoli(size):
    # create a list of letters that will be used
    list_of_letters = [chr(ord('a') + i) for i in range(size)]
    list_of_letters.reverse()
    width = size * 4 - 3

    # generate the rangoli pattern
    for i in range(size):
        # create the middle part of the row, which includes letters from both sides
        middle = '-'.join(list_of_letters[:i+1] + list_of_letters[:i][::-1])
        print(middle.center(width, '-'))

    # Now print the lower half of the rangoli, which is a reverse of the upper half
    for i in range(size-2, -1, -1):
        # create the middle part of the row, as done above
        middle = '-'.join(list_of_letters[:i+1] + list_of_letters[:i][::-1])
        print(middle.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)