import re

pattern = r'(\w+)@(\w+)\.(\w{2,3})'
text = "Please contact us at support@example.com for assistance."

match = re.search(pattern, text)

if match:
    print("Match found!")
    print("Match span:", match.span())  # Output: (22, 41), for example
    print("Match group:", match.group())  # Output: 'support@example.com'
    print("Match group 1:", match.group(1))  # Output: 'support'
    print("Match group 2:", match.group(2))  # Output: 'example'
    print("Match group 3:", match.group(3))  # Output: 'com'
else:
    print("No match found.")