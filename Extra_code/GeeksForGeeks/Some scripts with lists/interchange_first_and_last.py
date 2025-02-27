def interchange(l):
    # Create a new list
    new = []
    # Append the last elements as the first one
    new.append(l[-1])
    # Append the rest elements from the middle
    for _ in l[1:-1]:
        new.append(_)
    # Append the first element as the last one
    new.append(l[0])
    # Return
    return new


given_list = [12, 35, 9, 56, 24]
# given_list = [1, 2, 3]
print(interchange(given_list))