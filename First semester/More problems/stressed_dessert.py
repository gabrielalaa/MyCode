# Create another function which check if the string is really a word - but ONLY for this example
def check_word(string):
    # If the string starts with 'abc' is not a word
    if string.startswith('abc'):
        return False
    return True


def stressed_desserts(input_list):
    # Create an output list
    output_list = []
    for element in input_list:
        # Check if the element is alphabetical only
        if element.isalpha():
            # First step: check if the inverse (palindrome) element is in the list
            # Second step: check if the tuple with our element and its inverse (and vice versa) is in the output list
            # Third step: check if the element is really a string
            if element[::-1] in input_list and (element, element[::-1] not in output_list) and (element[::-1], element) not in output_list and check_word(element):
                output_list.append((element, element[::-1]))
    return output_list


words = ["abc", "cat", "bananna", "abcba", "121", "palindromes", "dollar", "abcdcba", "semordnilap", "tac", "stressed", "desserts"]
print(stressed_desserts(words))