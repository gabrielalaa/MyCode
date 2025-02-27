if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        sample = input().split()

        if sample[0] == 'insert':
            my_list.insert(int(sample[1]), int(sample[2]))
        elif sample[0] == 'print':
            print(my_list)
        elif sample[0] == 'remove':
            my_list.remove(int(sample[1]))
        elif sample[0] == 'append':
            my_list.append(int(sample[1]))
        elif sample[0] == 'sort':
            my_list.sort()
        elif sample[0] == 'pop':
            my_list.pop()
        else:
            my_list.reverse()
