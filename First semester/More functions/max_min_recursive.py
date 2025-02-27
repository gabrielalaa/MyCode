# Function for maximum
def maximum(l, i, n):
    # Base case: when the list has only one element
    if i == n - 1:
        return l[i]

    # Recursive case:
    # Find the maximum in the rest of the list
    m = maximum(l, i + 1, n)

    # Minimum is similar to maximum
    # Return the max of the current element and the maximum of the rest of the list
    return max(l[i], m)


# Take the input from the user
print("Your list is: ")
input_list = list(map(int, input().split()))
print(f"The maximum element is: {maximum(input_list, 0, len(input_list))}")