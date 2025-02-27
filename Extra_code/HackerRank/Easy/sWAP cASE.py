def swap_case(string):
    swap = ""
    for i in string:
        if i.isalpha():
            if i.isupper():
                swap += chr(ord(i) + 32)
            else:
                swap += chr(ord(i) - 32)
        else:
            swap += i

    return swap


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)