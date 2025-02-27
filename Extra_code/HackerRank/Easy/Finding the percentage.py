# {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # Reads a line of input from the user,
        # splits it into components (assuming space-separated values),
        # and performs unpacking
        name, *line = input().split()
        # The first part of the input is assigned to name
        # The rest of the parts are captured by '*line'
        # as a list

        # Converts the scores from string to float
        # map(function, item)
        # Converted back to a list in order to be used
        scores = list(map(float, line))

        # Stores the scores list in a dictionary
        # with the student's name as the key
        student_marks[name] = scores

    # The name of a student
    query_name = input()

    for key, values in student_marks.items():
        if key == query_name:
            # sum
            s = sum(values)
            # count
            c = len(values)
            # find the average
            a = s/c
            print(f'{a:.2f}')
            break