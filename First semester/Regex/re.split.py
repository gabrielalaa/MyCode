import re
# Assume text contains a list of lotto numbers separated by commas.
text = "Lotto numbers: 12, 18, 25, 34, 55"

# Using split to separate the numbers
numbers = re.split(r",\s*", text)

print(numbers)  # This will output ['Lotto numbers: 12', '18', '25', '34', '55']