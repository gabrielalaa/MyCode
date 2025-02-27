import re

# Compile a regular expression pattern for a simple email address
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# String to be searched
text_to_search = "Please contact us at contact@example.com for further information."

# Use the compiled pattern to search the string
match = email_pattern.search(text_to_search)

if match:
    print("Email found:", match.group())
else:
    print("No email found.")