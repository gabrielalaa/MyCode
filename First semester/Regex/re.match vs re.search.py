import re

text = "Email: user@example.com. Lotto numbers: 12, 18, 25, 34, 55"

# Using match
match_result = re.match(r"Lotto numbers", text)
search_result = re.search(r"Lotto numbers", text)

print("Match:", match_result)  # This will print "Match: None" because the text does not start with "Lotto numbers"
print("Search:", search_result.group())  # This will print "Search: Lotto numbers" because it can find the pattern
# anywhere in the text