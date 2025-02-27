import textwrap


def merge_the_tools(string, k):
    u = textwrap.wrap(string, k)
    for _ in u:
        my_list = []
        for letter in _:
            if letter not in my_list:
                my_list.append(letter)
        print(''.join(my_list))


# def merge_the_tools(string, k):
#     temp = []
#     len_temp = 0
#     for item in string:
#         len_temp += 1
#         if item not in temp:
#             temp.append(item)
#         if len_temp == k:
#             print (''.join(temp))
#             temp = []
#             len_temp = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)