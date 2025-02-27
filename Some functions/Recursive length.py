def length_of_string(string):
    if len(string) == 0:
        return 0
    else:
        # Count the last character and recurse the string without it
        return len(string[-1]) + length_of_string(string[:-1])
