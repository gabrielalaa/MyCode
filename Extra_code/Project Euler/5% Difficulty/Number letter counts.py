def number_to_words(n):
    # Words for the numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 11] if n > 10 else "ten"
    if n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    if n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + " hundred"
        else:
            return ones[n // 100] + " hundred and " + number_to_words(n % 100)
    if n == 1000:
        return "one thousand"


def count_letters(n):
    total_count = 0
    for number in range(1, n + 1):
        words = number_to_words(number)
        words = words.replace(" ", "").replace("-", "")  # Remove spaces and hyphens
        total_count += len(words)
    return total_count


# Example usage:
total_letters = count_letters(1000)
print("Total letters used from 1 to 1000:", total_letters)