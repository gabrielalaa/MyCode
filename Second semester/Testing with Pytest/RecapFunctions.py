def max_element(in_array):
    return max(in_array)

print(max_element([3, 16, 4, 32, 9]))

###

def check_orthogonal(a, b, c):
    # Sort the sides to identify the largest side
    sides = sorted([a, b, c])
    # Check for orthogonal triangle using Pythagoras' theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def check_negative_or_zero(in_array):
    for element in in_array:
        if element <= 0:
            return True
    return False


def triangles(a, b, c):
    if check_negative_or_zero([a, b, c]) or a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    elif a == b == c:
        return "Equilateral"
    elif (a == b) or (a == c) or (b == c):
        return "Equal-sided"
    elif check_orthogonal(a, b, c):
        return "Orthogonal"
    else:
        return "Others"

###

# White Box Testing
def greetme(signal):
    if signal > 5:
        greet = "hello"
    else:
        greet = "goodbye"
    return greet

###

# Black Box Testing
def revWord(sentence):
    list_sentence = sentence.split()
    return " ".join(list_sentence[::-1])

print(revWord("this is an interesting task"))