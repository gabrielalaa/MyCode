def generate_pascal_triangle(rows):
    triangle = []

    for i in range(rows):
        row = [None for _ in range(i+1)]
        # In each row the first and the last values are one
        row[0], row[-1] = 1, 1

        # Calculate the inner numbers
        for j in range(1, i):
            row[j] = triangle[i-1][j] + triangle[i-1][j-1]

        # Add each row in the triangle
        triangle.append(row)

    return triangle


# Take input
r = int(input("Enter the number of rows: "))
# Create the triangle
t = generate_pascal_triangle(r)
# Print each row
for row in t:
    print(*row)
