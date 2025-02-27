def maximum_path_sum(file):
    with open(file, 'r') as f:
        content = f.readlines()
        triangle = [[int(num) for num in line.strip().split()] for line in content]
        # print(triangle)  # [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

        # Start from the second to last row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            # print(triangle[i])
            # [2, 4, 6]
            # [7, 4]
            # [3]
            # Iterate through each number in the row
            for j in range(len(triangle[i])):
                # print(triangle[i][j])  # 2  4  6 ...
                # Update the current value to the maximum path sum by adding the maximum of the two possible paths below
                triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

        # The top element now contains the maximum path sum
        return triangle[0][0]

result = maximum_path_sum('triangle.txt')
print(result)