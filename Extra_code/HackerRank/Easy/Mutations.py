def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


# def mutate_string(string, position, character):
#     n = list(string)
#     n[position] = character
#     string = "".join(n)
#     return string

if __name__ == '__main__':
    # string
    s = input()
    # int position - index location
    # & a string character
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)