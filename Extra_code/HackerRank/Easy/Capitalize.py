def solve(string):
    my_l = string.split()
    new = []
    for name in my_l:
        if name[0].isupper():
            new.append(name)
        else:
            new.append(name[0].upper() + name[1:])
    return ' '.join(new)


# def solve(s):
#     for x in s[:].split():
#         s = s.replace(x, x.capitalize())
#     return s


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
