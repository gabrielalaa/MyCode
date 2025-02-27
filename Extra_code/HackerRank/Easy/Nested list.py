if __name__ == '__main__':

    # create lists for each to save them
    list_with_names = []
    list_with_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_with_names.append(name)
        list_with_scores.append(score)

    # find the lowest score
    m = min(list_with_scores)

    # find the second-lowest score
    # first, I converted the list into a set to remove duplicates
    new_list = list(set(list_with_scores))
    new_list.sort()
    second_m = new_list[1]
    # print(second_m)

    # create a list with the final names
    result = []

    # find the names
    my_d = dict(zip(list_with_names, list_with_scores))
    for key, value in my_d.items():
        if value == second_m:
            result.append(key)

    # sort the result alphabetically
    result.sort()

    # print it
    for i in result:
        print(i)