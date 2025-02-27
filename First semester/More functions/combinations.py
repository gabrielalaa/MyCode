# Print all possible combinations of r elements in a given array of size n
# Method 1
# from itertools import combinations
#
#
# def combine(array, r):
#     c = combinations(array, r)
#     return list(c)
#
#
# # Given size
# n = int(input())
# input_list = list(map(int, input().split()))
# # The number of elements to combine
# r = int(input())
# print(combine(input_list, r))


#################################################
# Method 2

# The main function that prints all
# combinations of size r in arr[] of
# size n. This function mainly uses
# combinationUtil()
def printCombination(arr, n, r):
    # A temporary array to store
    # all combination one by one
    data = [0] * r

    # Print all combination using
    # temporary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)


''' arr[] ---> Input Array
n     ---> Size of input array
r     ---> Size of a combination to be printed
index ---> Current index in data[]
data[] ---> Temporary array to store
            current combination
i     ---> index of current element in arr[]     '''


def combinationUtil(arr, n, r, index, data, i):
    # Current combination is ready,
    # print it
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    # When no more elements are
    # there to put in data[]
    if i >= n:
        return

    # current is included, put
    # next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1)

    # current is excluded, replace it
    # with next (Note that i+1 is passed,
    # but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    r = 3
    n = len(arr)
    printCombination(arr, n, r)


####################################################

# Method 3

def combine(arr, r):
    # A function to generate combinations
    def generate_combinations(arr, r, start, current, all_combinations):
        # When the combination is ready
        if len(current) == r:
            all_combinations.append(current[:])
            return
        for i in range(start, len(arr)):
            current.append(arr[i])
            generate_combinations(arr, r, i + 1, current, all_combinations)
            current.pop()  # Backtrack

    all_combinations = []
    generate_combinations(arr, r, 0, [], all_combinations)
    return all_combinations


# Given size
n = int(input("Enter size of array: "))
input_list = list(map(int, input("Enter the elements of the array separated by space: ").split()))
# The number of elements to combine
r = int(input("Enter number of elements to combine: "))
print(combine(input_list, r))