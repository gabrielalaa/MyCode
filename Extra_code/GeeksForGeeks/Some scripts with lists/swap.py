def swap (given, p1, p2):
    # We can simply swap the elements
    # Save the first one
    element1 = given[p1-1]
    given[p1-1] = given[p2]
    given[p2] = element1
    return given


# given_list = [23, 65, 19, 90]
given_list = [1, 2, 3, 4, 5]
pos1, pos2 = int(input()), int(input())
print(swap(given_list, pos1, pos2))