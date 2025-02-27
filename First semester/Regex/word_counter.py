# Import re - Use regular expressions to ignore any numeric values / special characters / symbols etc.
import re
# Import Counter to count the n most common words of a given length
from collections import Counter


def word_counter(filename, length, n):
    # Open and read the content from the file if it exists
    try:
        with open(filename, 'r') as f:
            # Ignore if the text file has upper/lower case
            content = f.read().lower()
    except FileNotFoundError:
        return 'File not found.'

    # Replace non-alphabetic characters with spaces
    content = re.sub(r'[^a-z\s]', ' ', content)

    # Create a list with words of len length based on our content list
    words = [word for word in content.split() if len(word) == length]

    # Count the words
    c = Counter(words)

    # Create a list with the n most common words of len length
    output_list = c.most_common(n)

    if output_list:
        return output_list
    else:
        return 'No words of given length'


# Take input
given_length, n_common_words = map(int, input().split())

print(word_counter('sample_text.txt', given_length, n_common_words))

######################################################################################

# Another solution
def wordCounter(fileName, length, n):
    try:
        with open(fileName, 'r') as file:
            text = file.read().lower()
            # Use regular expression to replace non-alphabetic characters with spaces
            text = re.sub(r'[^a-z\s]', ' ', text)
            # Split the text into words and filter by length
            words = [word for word in text.split() if len(word) == length]
            # Count the occurrences of each word
            word_counts = Counter(words)
            # Get the n most common words
            common_words = word_counts.most_common(n)
            # Check if there are no words of the given length
            if not common_words:
                print(f"No words of length {length} found.")
            return common_words
    except FileNotFoundError:
        print(f"The file {fileName} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


result = wordCounter('sample_text.txt', 4, 3)
print(result)