def power_digit_sum():
    s = 0
    num = 2**1000
    string_num = str(num)
    list_string_num = list(" ".join(string_num))
    for elem in list_string_num:
        if str(elem).isdecimal():
            s += int(elem)
    return s


print(power_digit_sum())
