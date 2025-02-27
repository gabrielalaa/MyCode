def average(array):
    # your code goes here
    # Convert it into a set to remove the duplicates
    array_set = set(array)
    print(array_set)
    return sum(array_set) / len(array_set)


if __name__ == '__main__':
    # the size of arr
    n = int(input())
    # n space-separated integers
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)