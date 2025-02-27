import csv
import re
from collections import Counter


def enron_emails(filename):
    # Read the content as a list of lists
    # with open(filename, 'r') as f:
    #     reader = list(csv.reader(f, delimiter=' '))
    with open(filename, 'r') as f:
        reader = csv.reader(f)  # Use the CSV reader to handle fields correctly
        next(reader)  # Skip the header

        senders = []
        receivers = []
        date = []
        ids = []
        subjects = []

        # # Ignore the first row, which is the header
        # for row in reader[1:]:
        #     # Create a string with each row
        #     string = ''.join(row)
        #
        #     # Make another list with each part of each row
        #     content = string.split(',')
        #     # print(content)
        #     senders.append(content[0])
        #     receivers.append(content[1])
        #     date.append(content[2])
        #     ids.append(content[3])
        #     subjects.append(content[4])
        for row in reader:
            senders.append(row[0])
            receivers.append(row[1])
            date.append(row[2])
            ids.append(row[3])
            subjects.append(row[4])

    # Print all the senders and receivers
    print(f"Senders: {senders}")
    print(f"Receivers: {receivers}")

    emails = senders + receivers
    # Find which email address is used the most and which TLD
    count_emails = Counter(emails)

    # This email address is used the most; but there are actually more with the same count
    maximum = count_emails.most_common(1)
    print(maximum)
    # # Save the max count
    # m = maximum[0][1]
    # for email, count in count_emails.items():

    used_most_often = count_emails.most_common()
    print(f'Used most often: {used_most_often}')

    # Find the most often used TLD
    # I will add only TLDs without the second-level domain
    tld = []
    for email in emails:
        pattern = r'(\w+)@(\w+)\.(\w{2,3})'
        match = re.search(pattern, email)
        if match:
            tld.append(match.group(3))
    # Count their appearance
    tld_count = Counter(tld)
    used_most_often_tld = tld_count.most_common(1)
    print(f'Used most often TLD : {used_most_often_tld}')

    # How many emails have the same 'from' and 'to'
    c_e = 0
    for i in range(0, len(senders)):
        if senders[i] == receivers[i]:
            c_e += 1
    print(f'{c_e} number of emails with the same sender and receiver')

    # Print dates ad ids in sorted manner
    # I don't get if I have to print them separately in a sorted way or based on the date only
    print(sorted(date))
    print(sorted(ids))

    # Based on the date only:
    new_dict = dict(zip(date, ids))
    # print(new_dict)
    print(sorted(new_dict.items(), key=lambda item: item[0]))

    subject_words = []
    for subject in subjects:
        # s = subject.split()
        # Split the subject into words based on non-word characters
        words = re.split(r'\W+', subject)
        subject_words.extend(words)
    # print(subject_words)
    word_count = Counter(subject_words)
    most_common_word = word_count.most_common(1)
    print(most_common_word)

    print(most_common_word[0][0])

    print(word_count.most_common())



enron_emails('enron_emails_sample.csv')