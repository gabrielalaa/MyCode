if __name__ == '__main__':
    # n = int(input())
    arr = list(map(int, input().split()))
    # Find the maximum - the first place
    m = max(arr)
    # Reverse the list
    arr.sort(reverse=True)
    # Find the second place
    for i in arr:
        if i < m:
            print(i)
            break