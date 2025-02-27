# Task 1 Sample Exam Question

import re
from collections import Counter

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

##############################################

#  Task 2
# to extract all sender emails – which email address is used most
# often, which TLD is used most often?

import re
from collections import Counter


def extract_emails_and_tlds(filename):
    # Regular expression for matching emails
    email_pattern = re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')

    # Read the file content
    with open(filename, 'r') as file:
        data = file.read()

    # Find all email addresses
    emails = email_pattern.findall(data)

    # Count the email addresses
    email_counts = Counter(emails)
    most_common_email = email_counts.most_common(1)

    # Extract the TLDs from the email addresses
    tlds = [email.split('.')[-1] for email in emails]

    # Count the TLDs
    tld_counts = Counter(tlds)
    most_common_tld = tld_counts.most_common(1)

    return most_common_email, most_common_tld

##############################################

# Task 3 - how many emails have the same
# “from” and “to” address

import re
from collections import Counter

def extract_receivers_and_count_same_from_to(filename):
    # Regular expression for matching emails
    email_pattern = re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')

    with open(filename, 'r') as file:
        data = file.read()

    # Assuming the file format has "From" and "To" labels for email addresses
    from_emails = email_pattern.findall(re.sub(r'To:\s*', '', data))
    to_emails = email_pattern.findall(re.sub(r'From:\s*', '', data))

    # Count the number of times the same email appears as both sender and receiver
    same_from_to_count = sum(1 for from_email, to_email in zip(from_emails, to_emails) if from_email == to_email)

    return from_emails, to_emails, same_from_to_count

# Usage example:
# filename = 'path_to_your_email_file.csv'
# from_emails, to_emails, same_from_to_count = extract_receivers_and_count_same_from_to(filename)
# print("From emails:", from_emails)
# print("To emails:", to_emails)
# print("Same 'from' and 'to' count:", same_from_to_count)

##############################################

# Task 4
# to extract all dates and message ids and print them in sorted
# manner (oldest to the newest)

import re
from datetime import datetime

def extract_dates_and_ids(filename):
    # Define a pattern for matching dates and message IDs
    # This is an example and may need to be adjusted based on the actual file format
    date_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')  # Example for dates in 'YYYY-MM-DD' format
    id_pattern = re.compile(r'\bID:\s*(\d+)\b')  # Example for IDs prefixed by 'ID: '

    with open(filename, 'r') as file:
        data = file.read()

    # Find all dates and IDs
    dates = date_pattern.findall(data)
    ids = id_pattern.findall(data)

    # Parse dates and pair with IDs
    paired_data = []
    for date_str, id_str in zip(dates, ids):
        date = datetime.strptime(date_str, '%Y-%m-%d')  # Adjust the date format as necessary
        paired_data.append((date, id_str))

    # Sort by date
    paired_data.sort()

    # Print in sorted order
    for date, id_str in paired_data:
        print(f"Date: {date.strftime('%Y-%m-%d')}, ID: {id_str}")

# Example usage:
# filename = 'path_to_your_data_file.txt'
# extract_dates_and_ids(filename)

##############################################

# Task 5
# to extract all subjects of the emails, what is the most commonly
# used word

import re
from collections import Counter

def extract_subjects_and_find_common_word(filename):
    # Regular expression for matching email subjects
    # This will depend on the format of your email file
    subject_pattern = re.compile(r'Subject: (.*)')

    with open(filename, 'r') as file:
        subjects = subject_pattern.findall(file.read())

    # Split subjects into words and count them
    word_counts = Counter(word.lower() for subject in subjects for word in subject.split())

    # Find the most common word
    most_common_word = word_counts.most_common(1)

    return most_common_word

# Example usage:
# filename = 'path_to_your_email_file.txt'
# common_word = extract_subjects_and_find_common_word(filename)
# print("The most commonly used word in the subjects is:", common_word)