import re
from collections import Counter


def most_common_names(fileName, n):
    # A basic regex pattern for a typical name
    name_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b'

    try:
        with open(fileName, 'r') as file:
            text = file.read()

            # Find all occurrences of the pattern
            names = re.findall(name_pattern, text)

            # Count each name's occurrences
            name_counts = Counter(names)

            # Return the n most common names
            return name_counts.most_common(n)

    except FileNotFoundError:
        print(f"The file {fileName} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# common_names = most_common_names('path_to_file.txt', 5)
# print(common_names)