from collections import Counter

# Nr. of shoes
X = int(input())
# List of shoe sizes
my_list = input().split()
# Convert the strings from the input list into integers
my_list = [int(integer) for integer in my_list]
# Nr. of customers
N = int(input())

# Count how many times the shoe size appear
my_dict = Counter(my_list)

# Read each customer in a list
customer_list = []
for _ in range(N):
    customer = input().split()
    customer_list.append(customer)

# (I realised that I can create the dict directly)
# (or I can even use map in this problem)
# Create another dictionary based on customer list
customer_dict = {}
for element in customer_list:
    key = int(element[0])
    value = int(element[1])
    if key in customer_dict:
        customer_dict[key].append(value)
    else:
        customer_dict[key] = [value]  # Initialize as a list with a single element

# Initialize the sum
s = 0

# Start counting the amount
for key, value in customer_dict.items():
    # If the shoe size is in the store, count the price and remove it from the shop
    if key in my_dict.keys():
        for v in value:
            if my_dict[key]:
                s += v
                my_dict[key] -= 1

print(s)

# print(my_dict)
# print(customer_dict)
# Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})
# {6: [55, 45, 55], 4: [40], 18: [60], 10: [50]}