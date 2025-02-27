def print_numbers_reverse(n):
    # Print the current number
    print(n)
    # Base case: if n is 0, we're done
    if n == 0:
        return
    else:
        # Recursive step: call the function with n-1
        print_numbers_reverse(n - 1)


# Example usage, printing numbers from 5 to 0:
print_numbers_reverse(5)