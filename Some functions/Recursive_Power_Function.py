def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * recursive_power(base, exponent - 1)


result = recursive_power(2, 8)
print(result)  # Output will be 256
