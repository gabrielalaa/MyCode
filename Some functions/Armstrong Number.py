def armstrong(n):
    # Save a copy of n
    copy = n
    # Initialize the sum as m
    m = 0
    # Calculate the m using the rule
    while n:
        # Add the cube of the last digit
        m += (n % 10) ** 3
        # Remove the last digit
        n //= 10
    if copy == m:
        return True
    return False


number = int(input("Enter a number: "))
if armstrong(number):
    print(f'{number} is an Armstrong number.')
else:
    print(f'{number} is not a Armstrong number.')
